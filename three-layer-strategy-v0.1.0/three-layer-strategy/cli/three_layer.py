#!/usr/bin/env python3
"""Zero-dependency project initializer for Three-Layer Strategy."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_TEMPLATE = REPO_ROOT / "project-template"
FRAMEWORK_TEMPLATES = REPO_ROOT / "framework" / "templates"
CHANGE_FILES = ("intent.md", "assessment.md", "spec.md", "plan.md", "tasks.md", "verification.md")
ADAPTER_TARGETS = {
    "codex": (REPO_ROOT / "adapters" / "codex" / "AGENTS.md", Path("AGENTS.md")),
    "claude": (REPO_ROOT / "adapters" / "claude-code" / "CLAUDE.md", Path("CLAUDE.md")),
    "cursor": (REPO_ROOT / "adapters" / "cursor" / "three-layer.mdc", Path(".cursor/rules/three-layer.mdc")),
    "copilot": (REPO_ROOT / "adapters" / "copilot" / "copilot-instructions.md", Path(".github/copilot-instructions.md")),
}


def copy_file(source: Path, target: Path, force: bool) -> str:
    if target.exists() and not force:
        return f"skip  {target} (already exists)"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return f"write {target}"


def iter_template_files() -> list[Path]:
    return sorted(path for path in PROJECT_TEMPLATE.rglob("*") if path.is_file())


def command_init(args: argparse.Namespace) -> int:
    target = Path(args.path).resolve()
    target.mkdir(parents=True, exist_ok=True)
    messages = []
    for source in iter_template_files():
        relative = source.relative_to(PROJECT_TEMPLATE)
        if relative == Path("AGENTS.md") and args.adapter == "codex":
            continue
        messages.append(copy_file(source, target / relative, args.force))

    adapters = ADAPTER_TARGETS.keys() if args.adapter == "all" else (args.adapter,)
    if args.adapter != "none":
        for adapter in adapters:
            source, relative = ADAPTER_TARGETS[adapter]
            messages.append(copy_file(source, target / relative, args.force))

    print("\n".join(messages))
    print(f"Initialized Three-Layer Strategy in {target}")
    return 0


def render_template(source: Path, title: str, owner: str) -> str:
    return (
        source.read_text(encoding="utf-8")
        .replace("{{ title }}", title)
        .replace("{{ owner }}", owner)
        .replace("{{ date }}", dt.date.today().isoformat())
    )


def command_new_change(args: argparse.Namespace) -> int:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        print("error: slug must use lowercase letters, digits and single hyphens", file=sys.stderr)
        return 2
    project = Path(args.project).resolve()
    aidd = project / ".aidd"
    if not aidd.is_dir():
        print("error: project is not initialized; run 'init' first", file=sys.stderr)
        return 2
    change = aidd / "changes" / args.slug
    if change.exists() and not args.force:
        print(f"error: {change} already exists; pass --force to fill missing files", file=sys.stderr)
        return 2
    change.mkdir(parents=True, exist_ok=True)
    for filename in CHANGE_FILES:
        target = change / filename
        if target.exists() and not args.force:
            continue
        source = FRAMEWORK_TEMPLATES / filename
        target.write_text(render_template(source, args.title, args.owner), encoding="utf-8")
        print(f"write {target}")
    print(f"Created change bundle: {change}")
    return 0


def doctor_errors(project: Path) -> list[str]:
    required = (
        project / "AGENTS.md",
        project / ".aidd" / "config.yaml",
        project / ".aidd" / "principles.md",
        project / ".aidd" / "specs",
        project / ".aidd" / "changes",
        project / ".aidd" / "decisions",
    )
    errors = [f"missing {path.relative_to(project)}" for path in required if not path.exists()]
    changes = project / ".aidd" / "changes"
    if changes.is_dir():
        for folder in sorted(path for path in changes.iterdir() if path.is_dir()):
            for filename in CHANGE_FILES:
                if not (folder / filename).is_file():
                    errors.append(f"incomplete change {folder.name}: missing {filename}")
    return errors


def command_doctor(args: argparse.Namespace) -> int:
    project = Path(args.path).resolve()
    errors = doctor_errors(project)
    if errors:
        print("Three-Layer doctor found problems:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Three-Layer structure is healthy: {project}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="three-layer", description="Three-Layer Strategy project tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="initialize a project")
    init_parser.add_argument("path", nargs="?", default=".")
    init_parser.add_argument("--adapter", choices=("codex", "claude", "cursor", "copilot", "all", "none"), default="all")
    init_parser.add_argument("--force", action="store_true", help="overwrite existing framework files")
    init_parser.set_defaults(func=command_init)

    change_parser = subparsers.add_parser("new-change", help="create a change bundle")
    change_parser.add_argument("slug")
    change_parser.add_argument("--project", default=".")
    change_parser.add_argument("--title", required=True)
    change_parser.add_argument("--owner", default="TBD")
    change_parser.add_argument("--force", action="store_true", help="overwrite bundle template files")
    change_parser.set_defaults(func=command_new_change)

    doctor_parser = subparsers.add_parser("doctor", help="validate project structure")
    doctor_parser.add_argument("path", nargs="?", default=".")
    doctor_parser.set_defaults(func=command_doctor)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
