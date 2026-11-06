"""从空数据验证命令行工作流，不修改随附演示数据。"""
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parent


def main():
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    with TemporaryDirectory() as folder:
        data = Path(folder) / 'my_tasks.json'
        output = Path(folder) / 'report'
        commands = [
            ['add', '--title', '完成变量练习', '--day', '1', '--minutes', '45'],
            ['add', '--title', '完成循环练习', '--day', '2', '--minutes', '60'],
            ['done', '--id', '1', '--actual', '40'],
            ['list'],
            ['report', '--output', str(output)],
        ]
        for args in commands:
            result = subprocess.run(
                [sys.executable, str(ROOT / 'study_tracker.py'), '--data', str(data), *args],
                env=env, capture_output=True, text=True, encoding='utf-8', timeout=15,
            )
            if result.returncode:
                raise RuntimeError(result.stderr)
            print(result.stdout.strip())
        summary = json.loads((output / 'summary.json').read_text(encoding='utf-8'))
        expected = dict(total=2, completed=1, percent=50.0,
                        planned_minutes=105, actual_minutes=40)
        if summary != expected:
            raise AssertionError((summary, expected))
        if not all((output / name).exists() for name in ['report.html', 'tasks.csv', 'summary.json']):
            raise AssertionError('缺少导出文件')
        print('从空数据到导出报告：全部通过')


if __name__ == '__main__':
    main()
