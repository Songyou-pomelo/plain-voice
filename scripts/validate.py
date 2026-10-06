"""Dependency-free package and core/prompt consistency validation."""
from pathlib import Path
import re

def validate(root):
    errors=[]
    required=['SKILL.md','README.md','LICENSE','prompts/universal.txt','agents/openai.yaml','evals/cases.md']
    for name in required:
        if not (root/name).is_file(): errors.append('Missing '+name)
    if errors: return errors
    skill=(root/'SKILL.md').read_text(encoding='utf-8')
    match=re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n',skill)
    if not match or match.group(1)!='plain-voice': errors.append('Invalid expected frontmatter')
    expected='请对接下来的中文创作与编辑任务使用以下规则。\n\n'+skill.split('---',2)[2].strip()+'\n'
    if (root/'prompts/universal.txt').read_text(encoding='utf-8')!=expected: errors.append('Prompt differs from core')
    return errors

if __name__=='__main__':
    errors=validate(Path(__file__).resolve().parents[1])
    print('\n'.join(errors) if errors else 'PASS: package structure and prompt consistency; model behavior not tested')
    raise SystemExit(bool(errors))
