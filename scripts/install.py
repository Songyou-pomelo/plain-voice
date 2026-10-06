"""Install only the self-contained skill into an explicitly selected project."""
import argparse
import shutil
from pathlib import Path

def install(platform, project):
    source = Path(__file__).resolve().parents[1]
    target_root = Path(project).expanduser().resolve()
    if not target_root.is_dir():
        raise ValueError('Project directory must already exist')
    folder = '.agents' if platform == 'codex' else '.claude'
    destination = target_root / folder / 'skills' / 'plain-voice'
    if destination.exists():
        raise FileExistsError('Existing skill is preserved; back it up and replace manually')
    destination.mkdir(parents=True)
    shutil.copy2(source / 'SKILL.md', destination / 'SKILL.md')
    if platform == 'codex':
        shutil.copytree(source / 'agents', destination / 'agents')
    return destination

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--platform', choices=['codex', 'claude'], required=True)
    parser.add_argument('--project', required=True)
    args = parser.parse_args()
    try:
        print(install(args.platform, args.project))
    except (ValueError, FileExistsError, OSError) as exc:
        parser.exit(1, str(exc)+'\n')
