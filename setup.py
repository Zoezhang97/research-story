BUILD_DIR=$1

# Exit early if app is clearly not Python.
if [ ! -f "$BUILD_DIR/requirements.txt" ] && [ ! -f "$BUILD_DIR/setup.py" ] && [ ! -f "$BUILD_DIR/Pipfile" ]; then
  exit 1
fi

echo Python