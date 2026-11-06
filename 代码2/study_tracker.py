"""七天综合项目：学习任务管理器。仅依赖Python标准库。
python study_tracker.py demo
python study_tracker.py list
python study_tracker.py add --title "复习函数" --day 3 --minutes 30
python study_tracker.py done --id 8 --actual 25
python study_tracker.py report
"""
import argparse
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def validate(tasks):
    if not isinstance(tasks, list):
        raise ValueError('数据根节点必须是列表')
    seen = set()
    for item in tasks:
        if not isinstance(item, dict):
            raise ValueError('任务必须是对象')
        if type(item.get('id')) is not int or item['id'] <= 0 or item['id'] in seen:
            raise ValueError('任务ID必须是唯一正整数')
        seen.add(item['id'])
        if not isinstance(item.get('title'), str) or not item['title'].strip():
            raise ValueError('任务名称不能为空')
        if type(item.get('day')) is not int or not 1 <= item['day'] <= 7:
            raise ValueError('学习日必须在1到7之间')
        if type(item.get('minutes')) is not int or item['minutes'] <= 0:
            raise ValueError('计划分钟必须为正整数')
        if type(item.get('actual')) is not int or item['actual'] < 0:
            raise ValueError('实际分钟必须为非负整数')
        if type(item.get('done')) is not bool:
            raise ValueError('完成状态必须为布尔值')
    return tasks

def load(path):
    if not path.exists():
        return []
    return validate(json.loads(path.read_text(encoding='utf-8')))

def save(path, tasks):
    validate(tasks)
    path.parent.mkdir(parents=True, exist_ok=True)
    # 先写临时文件再替换，减少写到一半损坏原数据的风险。
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)

def add_task(tasks, title, day, minutes):
    item = {'id': max((t['id'] for t in tasks), default=0) + 1,
            'title': title.strip(), 'day': day, 'minutes': minutes,
            'actual': 0, 'done': False}
    updated = tasks + [item]
    validate(updated)
    return updated

def complete(tasks, task_id, actual):
    if actual < 0:
        raise ValueError('实际分钟不能为负')
    found = False
    updated = []
    for task in tasks:
        item = dict(task)
        if item['id'] == task_id:
            item.update(done=True, actual=actual)
            found = True
        updated.append(item)
    if not found:
        raise ValueError(f'不存在任务ID：{task_id}')
    return validate(updated)

def summarize(tasks):
    completed = sum(task['done'] for task in tasks)
    return {'total': len(tasks), 'completed': completed,
            'percent': round(100 * completed / len(tasks), 1) if tasks else 0,
            'planned_minutes': sum(task['minutes'] for task in tasks),
            'actual_minutes': sum(task['actual'] for task in tasks)}

def demo_tasks():
    topics = ['变量与输入输出', '判断循环与容器', '函数与异常', '文件与模块',
              '面向对象与数据整理', 'HTTP与本地接口', '综合项目与验收']
    return [{'id': i, 'title': title, 'day': i, 'minutes': 210,
             'actual': 210 if i <= 5 else 0, 'done': i <= 5}
            for i, title in enumerate(topics, 1)]

def export(tasks, folder):
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / 'tasks.csv').open('w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id','title','day','minutes','actual','done'])
        writer.writeheader()
        writer.writerows(tasks)
    summary = summarize(tasks)
    (folder / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    rows = ''.join(f'<tr><td>{t["id"]}</td><td>{html.escape(t["title"])}</td>'
                   f'<td>第{t["day"]}天</td><td>{t["minutes"]}</td><td>{t["actual"]}</td>'
                   f'<td>{"已完成" if t["done"] else "待学习"}</td></tr>' for t in tasks)
    bars = ''
    for day in range(1, 8):
        selected = [t for t in tasks if t['day'] == day]
        plan = sum(t['minutes'] for t in selected)
        actual = sum(t['actual'] for t in selected)
        width = min(100, 100 * actual / plan) if plan else 0
        bars += f'<div class="bar"><b>Day {day}</b><div class="track"><i style="width:{width}%"></i></div><span>{actual}/{plan} 分钟</span></div>'
    page = f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Python学习报告</title><style>body{{font:16px/1.7 system-ui,"Microsoft YaHei";background:#f3f6fb;color:#183048;margin:0}}main{{max-width:1000px;margin:auto;padding:32px}}h1{{font-size:32px}}.cards{{display:flex;gap:16px;flex-wrap:wrap}}.card{{background:white;padding:20px;border-radius:12px;flex:1}}.card strong{{font-size:28px;display:block;color:#126d74}}section{{background:white;padding:24px;margin-top:24px;border-radius:12px}}table{{border-collapse:collapse;width:100%}}td,th{{padding:10px;border-bottom:1px solid #e0e7ed;text-align:left}}.bar{{display:flex;align-items:center;gap:16px;margin:12px 0}}.track{{background:#e9eff5;flex:1;height:14px;border-radius:8px;overflow:hidden}}i{{display:block;background:#14978d;height:100%}}.bar span{{width:145px}}small{{color:#627489}}</style>
<main><small>PYTHON · 七天综合项目 · 演示数据，不代表你的真实学习进度</small><h1>学习任务与进度报告</h1>
<div class="cards"><div class="card">完成任务<strong>{summary['completed']} / {summary['total']}</strong></div>
<div class="card">任务完成率<strong>{summary['percent']}%</strong></div>
<div class="card">实际学习<strong>{summary['actual_minutes']} 分钟</strong></div></div>
<section><h2>每日实际 / 计划</h2>{bars}</section><section><h2>任务清单</h2><table><tr><th>ID</th><th>内容</th><th>学习日</th><th>计划分钟</th><th>实际分钟</th><th>状态</th></tr>{rows}</table></section></main></html>'''
    (folder / 'report.html').write_text(page, encoding='utf-8')
    return summary

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=ROOT / 'project_data' / 'tasks.json')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('demo', help='首次写入演示数据；不会覆盖已有文件')
    commands.add_parser('list')
    add = commands.add_parser('add')
    add.add_argument('--title', required=True)
    add.add_argument('--day', required=True, type=int)
    add.add_argument('--minutes', required=True, type=int)
    done = commands.add_parser('done')
    done.add_argument('--id', required=True, type=int)
    done.add_argument('--actual', required=True, type=int)
    report = commands.add_parser('report')
    report.add_argument('--output', type=Path, default=ROOT / 'project_output')
    args = parser.parse_args(argv)
    try:
        if args.command == 'demo':
            if args.data.exists():
                raise ValueError('数据文件已存在；请使用 --data 指定一个新文件')
            tasks = demo_tasks()
            save(args.data, tasks)
            print('已创建7条演示任务，其中5条已完成。')
        else:
            tasks = load(args.data)
            if args.command == 'add':
                tasks = add_task(tasks, args.title, args.day, args.minutes)
                save(args.data, tasks)
                print('新增任务ID:', tasks[-1]['id'])
            elif args.command == 'done':
                tasks = complete(tasks, args.id, args.actual)
                save(args.data, tasks)
                print('任务已完成:', args.id)
            elif args.command == 'list':
                for task in tasks:
                    print(f'{task["id"]:02} | 第{task["day"]}天 | {task["title"]} | {"已完成" if task["done"] else "待学习"}')
            else:
                print(json.dumps(export(tasks, args.output), ensure_ascii=False))
                print('已生成 report.html、tasks.csv、summary.json')
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(2, f'错误：{error}\n')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
