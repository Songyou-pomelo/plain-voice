import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
class Tests(unittest.TestCase):
    def test_package_consistent(self): self.assertEqual(load('validate').validate(ROOT),[])
    def test_scan_is_advisory(self):
        text='讨论能量守恒\n你要明白';got=load('lint_text').scan(text)
        self.assertEqual(got[0]['line'],1);self.assertTrue(got[0]['review_required']);self.assertEqual(got[1]['line'],2)
    def test_install_and_no_overwrite(self):
        module=load('install')
        with tempfile.TemporaryDirectory() as d:
            target=module.install('codex',d)
            self.assertTrue((target/'agents'/'openai.yaml').exists())
            (target/'SKILL.md').write_text('user content',encoding='utf-8')
            with self.assertRaises(FileExistsError): module.install('codex',d)
            self.assertEqual((target/'SKILL.md').read_text(encoding='utf-8'),'user content')
    def test_claude_install(self):
        with tempfile.TemporaryDirectory() as d:
            target=load('install').install('claude',d)
            self.assertEqual(target.parts[-3:],('.claude','skills','plain-voice'))
            self.assertFalse((target/'agents').exists())
if __name__=='__main__':unittest.main()
