"""Advisory phrase scan; never rewrites text or assesses AI authorship."""
import argparse,json,re
from pathlib import Path
PHRASES=['你要明白','你必须懂得','你应该清醒一点','直到后来我才明白','那一刻，我突然懂了','自己琢磨了一下发现','时间会给出答案','成为更好的自己','与自己和解','赋能','助力','底层逻辑','深度洞察','认知跃迁','松弛感','能量','内核','颠覆性','前所未有']
def scan(text):
    findings=[]
    for number,line in enumerate(text.splitlines(),1):
        for phrase in PHRASES:
            for m in re.finditer(re.escape(phrase),line):
                findings.append({'line':number,'column':m.start()+1,'phrase':phrase,'review_required':True})
    return findings
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file');args=p.parse_args()
    print(json.dumps({'scope':'advisory subset, not all six categories','findings':scan(Path(args.file).read_text(encoding='utf-8'))},ensure_ascii=False,indent=2))
