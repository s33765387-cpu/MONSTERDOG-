#!/usr/bin/env bash
set -eu

echo "Packaging monsterdog packages into zips..."
BASE_DIR="$(pwd)"
PACK_DIR="$BASE_DIR/packages/monsterdog"

if [ ! -d "$PACK_DIR" ]; then
  echo "No packages/monsterdog directory found" >&2
  exit 1
fi

cd "$PACK_DIR"

for d in */ ; do
  [ -d "$d" ] || continue
  name="${d%/}"
  zipfile="$PACK_DIR/$name.zip"
  echo "Creating $zipfile from $d"
  rm -f "$zipfile"
  zip -r "$zipfile" "$d" >/dev/null
done

echo "Packaging complete. Artifacts placed in packages/monsterdog/*.zip"
