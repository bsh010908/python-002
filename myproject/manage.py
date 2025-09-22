#!/usr/bin/env python
"""
Django command-line utility for administrative tasks.
Refactored version with clearer error handling and optional .env support.
"""

import os
import sys


def main() -> None:
    """Run administrative tasks."""
    # ✅ 환경 변수 기본값 지정
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    try:
        # ✅ dotenv 지원 (pip install python-dotenv 필요)
        from dotenv import load_dotenv
        load_dotenv()  # .env 파일 로드 (있을 경우)

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "❌ Django를 불러올 수 없습니다. 가상환경이 활성화되었는지 확인하세요.\n"
            "   pip install -r requirements.txt 실행이 필요할 수 있습니다."
        ) from exc

    # ✅ 명령 실행
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
