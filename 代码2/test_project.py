import unittest
import tempfile
from pathlib import Path
import study_tracker as app

class ProjectTests(unittest.TestCase):
    def test_add_complete_persist(self):
        tasks = app.add_task([], '  文件练习  ', 4, 30)
        completed = app.complete(tasks, 1, 25)
        self.assertFalse(tasks[0]['done'])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'tasks.json'
            app.save(path, completed)
            self.assertEqual(app.load(path), completed)

    def test_invalid_input(self):
        for title, day, minutes in [('', 1, 20), ('任务', 8, 20), ('任务', 1, -1)]:
            with self.assertRaises(ValueError):
                app.add_task([], title, day, minutes)
        with self.assertRaises(ValueError):
            app.complete([], 99, 5)

    def test_empty_and_demo(self):
        self.assertEqual(app.summarize([])['percent'], 0)
        self.assertEqual(app.summarize(app.demo_tasks()),
                         dict(total=7, completed=5, percent=71.4, planned_minutes=1470, actual_minutes=1050))

    def test_export_escapes_html_and_keeps_csv(self):
        tasks = app.add_task([], '<script>alert(1)</script>', 1, 20)
        with tempfile.TemporaryDirectory() as folder:
            app.export(tasks, Path(folder))
            content = (Path(folder) / 'report.html').read_text(encoding='utf-8')
            self.assertNotIn('<script>alert', content)
            self.assertIn('&lt;script&gt;', content)
            self.assertTrue((Path(folder) / 'tasks.csv').exists())

    def test_corrupt_data(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'tasks.json'
            path.write_text('not json', encoding='utf-8')
            with self.assertRaises(ValueError):
                app.load(path)

if __name__ == '__main__':
    unittest.main()
