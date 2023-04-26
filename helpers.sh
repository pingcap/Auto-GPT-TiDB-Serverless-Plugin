#!/usr/bin/env bash

clean() {
  # Remove build artifacts and temporary files
  rm -rf build 2>/dev/null || true
  rm -rf dist 2>/dev/null || true
  rm -rf __pycache__ 2>/dev/null || true
  rm -rf *.egg-info 2>/dev/null || true
  rm -rf **/*.egg-info 2>/dev/null || true
  rm -rf *.pyc 2>/dev/null || true
  rm -rf **/*.pyc 2>/dev/null || true
  rm -rf reports 2>/dev/null || true
}


style() {
  # Format code
  isort .
  black --exclude=".*\/*(dist|venv|.venv|test-results)\/*.*" .
}

if [ "$1" = "clean" ]; then
  echo Removing build artifacts and temporary files...
  clean
elif [ "$1" = "style" ]; then
  echo Running code formatters...
  style
else
  echo "Usage: $0 [clean|qa|style]"
  exit 1
fi

echo Done!
echo
exit 0