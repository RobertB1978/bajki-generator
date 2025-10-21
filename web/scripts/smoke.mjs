/* eslint-env node */
import assert from "node:assert";

const base = process.env.SMOKE_BASE || "http://127.0.0.1:4173";

const r = await fetch(`${base}/api/health`);
assert.equal(r.status, 200);

const r2 = await fetch(`${base}/api/stories`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ hero: "Ala", mood: "pogodny" })
});
assert.equal(r2.status, 200);

console.log("SMOKE OK");
