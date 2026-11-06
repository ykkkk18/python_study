"""运行100个示例并保存真实输出：python run_all.py。"""
from pathlib import Path
import json,subprocess,sys,os

def main():
    root = Path(__file__).parent
    results = []
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    for path in sorted(root.glob('lesson_*.py')):
        result = subprocess.run([sys.executable, str(path)], cwd=root,
                                capture_output=True, text=True, encoding='utf-8',
                                errors='replace', timeout=35, env=env)
        record = {'episode': int(path.stem.split('_')[1]), 'file': path.name,
                  'returncode': result.returncode, 'stdout': result.stdout,
                  'stderr': result.stderr}
        results.append(record)
        print(path.name, 'PASS' if result.returncode == 0 else 'FAIL', flush=True)
    (root / '运行结果.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    failed = [x for x in results if x['returncode']]
    print(f'完成：{len(results)-len(failed)}/{len(results)}')
    return bool(failed)

if __name__ == '__main__':
    raise SystemExit(main())
