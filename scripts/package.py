from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
out=root/'dist';out.mkdir(exist_ok=True)
target=out/'plain-voice-skill-0.3.0.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for relative in ['SKILL.md','agents/openai.yaml','LICENSE']:
        z.write(root/relative,'plain-voice/'+relative)
print(target)
