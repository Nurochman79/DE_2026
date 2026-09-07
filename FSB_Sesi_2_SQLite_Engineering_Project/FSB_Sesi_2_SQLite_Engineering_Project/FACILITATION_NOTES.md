# Reviewer Notes — Engineering Simulation

Gunakan repository ini sebagai simulasi ticket delivery, bukan sesi code-along.

## Peran
- Peserta bertindak sebagai engineer owner untuk ticket DATA-214.
- Fasilitator bertindak sebagai tech lead/reviewer.
- Bantuan diberikan melalui pertanyaan review, log, failing check, dan contract—bukan langkah mengetik solusi.

## Review Cadence
1. **Ticket kickoff:** engineer menyampaikan pemahaman scope dan risiko.
2. **Design checkpoint:** reviewer menilai grain, keys, constraints, dan load policy.
3. **Implementation checkpoint:** engineer menunjukkan failing/passing quality gate yang relevan.
4. **PR review:** reviewer meminta evidence build bersih, reject handling, dan metric logic.
5. **Handoff:** engineer menjelaskan recovery dan reproducibility.

## Reviewer Prompts
- Tunjukkan bukti FK benar-benar enforced, bukan hanya dideklarasikan.
- Apa blast radius jika satu transaction invalid?
- Di mana transaction boundary berada?
- Bagaimana membuktikan revenue tidak mengalami row multiplication?
- Apa yang terjadi jika pipeline dijalankan dua kali?
- Artifact mana yang akan dipakai downstream?

## Escalation Ladder
1. Minta engineer membaca error/output.
2. Minta kaitkan failure dengan acceptance criterion.
3. Minta satu hipotesis yang bisa diuji.
4. Jalankan quality gate paling sempit.
5. Berikan boundary atau contract hint; jangan berikan baris solusi.

## Anti-Patterns
- live coding solusi penuh;
- memberi expected SQL sebelum engineer menjelaskan grain;
- menerima hasil notebook tanpa clean CLI build;
- mengabaikan reject karena angka final terlihat benar;
- menyebut setiap langkah sebagai materi/latihan/kelas pada dokumen peserta.
