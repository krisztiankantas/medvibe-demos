# MedVibe – ügyfél-demóoldalak

Minden új rendelőhöz egy saját oldal készül, amelyen a rendelő Rita demó-agentjét a böngészőből ki lehet próbálni.
Cím: `https://<user>.github.io/medvibe-demos/<slug>/`

## Új ügyfél oldala

1. `clients/<slug>.json` létrehozása (minta: `clients/diamonddentart.json`)
2. `python3 generate.py clients/<slug>.json` → elkészül a `<slug>/index.html`
3. Commit + push → GitHub Pages 1–2 percen belül kiteszi.

A gyökér `index.html` a medvibe.net-re irányít, így a demók listája nem látható. Az oldalak `noindex` jelölésűek.
