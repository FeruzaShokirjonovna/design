#!/usr/bin/env python
import os
import sys

def main():
    """Completing management issues"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'design.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django ni import qila olmadim. Django o'rnatilganligiga va "
            "PYTHONPATH muhit o'zgaruvchingizda mavjudligiga ishonch hosil qiling. "
            "Yoki virtual muhitni ishga tushirishni unutdingizmi?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
