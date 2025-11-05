#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const MonsterdogEntity = require('../src/entities/monsterdog');

const manifestsDir = path.join(__dirname, '..', 'manifests', 'monsterdog');
const files = fs.readdirSync(manifestsDir).filter(f => f.endsWith('.json'));
const manifests = files.map(f => {
  try { return JSON.parse(fs.readFileSync(path.join(manifestsDir, f), 'utf8')); }
  catch (e) { console.error('Invalid JSON in', f); process.exit(2); }
});

const entity = new MonsterdogEntity();
entity.activate();
const actions = entity.getAgenticActions().map(a => a.name).sort();
const manifestNames = manifests.map(m => m.name).sort();

console.log('Found', actions.length, 'entity actions and', manifestNames.length, 'manifests');

let ok = true;
actions.forEach(name => {
  if (!manifestNames.includes(name)) {
    console.error('Missing manifest for action:', name);
    ok = false;
  }
});

manifests.forEach(m => {
  if (!actions.includes(m.name)) {
    console.error('Manifest present for unknown action:', m.name);
    ok = false;
  }
});

if (!ok) {
  console.error('\nManifest validation FAILED');
  process.exit(1);
}

console.log('\nManifest validation PASSED');
process.exit(0);
