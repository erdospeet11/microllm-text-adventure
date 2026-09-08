const picker = document.getElementById("picker");
const play = document.getElementById("play");
const grid = document.getElementById("genre-grid");
const pickerError = document.getElementById("picker-error");
const logEl = document.getElementById("log");
const choicesEl = document.getElementById("choices");
const form = document.getElementById("cmd");
const input = document.getElementById("cmd-input");
const newGameBtn = document.getElementById("new-game");
const endingBanner = document.getElementById("ending-banner");
const hudLoc = document.getElementById("hud-loc");
const hudHp = document.getElementById("hud-hp");
const hudTension = document.getElementById("hud-tension");
const barHp = document.getElementById("bar-hp");
const barTension = document.getElementById("bar-tension");
const hudInv = document.getElementById("hud-inv");
const hudFlags = document.getElementById("hud-flags");

let sessionId = null;
let gameOver = false;
let currentChoices = [];

async function fetchJSON(url, options) {
  const res = await fetch(url, options);
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const detail = data.detail;
    const msg = typeof detail === "string" ? detail : JSON.stringify(detail || res.statusText);
    throw new Error(msg);
  }
  return data;
}

function showError(el, message) {
  el.hidden = false;
  el.textContent = message;
}

function addEntry(text, className) {
  const div = document.createElement("div");
  div.className = `entry ${className || ""}`.trim();
  text.split(/\n\n+/).forEach((block) => {
    const p = document.createElement("p");
    p.textContent = block;
    div.appendChild(p);
  });
  logEl.appendChild(div);
  logEl.scrollTop = logEl.scrollHeight;
}

function renderChoices(choices) {
  currentChoices = choices || [];
  choicesEl.innerHTML = "";
  currentChoices.forEach((choice) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "choice";
    btn.innerHTML = `<kbd>[${choice.id.toUpperCase()}]</kbd>`;
    btn.append(document.createTextNode(choice.label));
    btn.addEventListener("click", () => submitTurn(choice.id, choice.label));
    choicesEl.appendChild(btn);
  });
}

function renderHud(state) {
  hudLoc.textContent = state.location || "—";
  const hp = state.stats?.hp ?? 0;
  const tension = state.stats?.tension ?? 0;
  hudHp.textContent = hp;
  hudTension.textContent = tension;
  barHp.style.transform = `scaleX(${Math.max(0, Math.min(1, hp / 10))})`;
  barTension.style.transform = `scaleX(${Math.max(0, Math.min(1, tension / 10))})`;
  hudInv.innerHTML = "";
  if (!state.inventory?.length) {
    const li = document.createElement("li");
    li.textContent = "(empty)";
    hudInv.appendChild(li);
  } else {
    state.inventory.forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      hudInv.appendChild(li);
    });
  }
  hudFlags.innerHTML = "";
  const flags = state.flags || {};
  const keys = Object.keys(flags).filter((k) => k !== "last_choice");
  if (!keys.length) {
    hudFlags.textContent = "—";
    return;
  }
  keys.forEach((key) => {
    const span = document.createElement("span");
    span.className = "flag";
    span.textContent = `${key}:${flags[key]}`;
    hudFlags.appendChild(span);
  });
}

function applyEnvelope(envelope, playerLine) {
  const { turn, state } = envelope;
  sessionId = envelope.session_id;
  gameOver = Boolean(turn.game_over);
  document.body.dataset.genre = state.genre;
  document.body.dataset.visual = turn.visual_key || "threshold";
  if (playerLine) addEntry(`> ${playerLine}`, "player");
  addEntry(turn.narration, turn.game_over ? "ending-entry" : "narrator");
  renderHud(state);
  renderChoices(gameOver ? [] : turn.choices);
  input.disabled = gameOver;
  form.querySelector("button").disabled = gameOver;
  if (turn.game_over) {
    endingBanner.hidden = false;
    endingBanner.textContent = `END FILE // ${turn.ending || "closed"}`;
  } else {
    endingBanner.hidden = true;
    endingBanner.textContent = "";
  }
}

async function startGame(genreId, title) {
  pickerError.hidden = true;
  const envelope = await fetchJSON("/api/new", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ genre: genreId }),
  });
  logEl.innerHTML = "";
  addEntry(`CASSETTE MOUNTED: ${title || genreId}`, "system");
  picker.hidden = true;
  play.hidden = false;
  newGameBtn.hidden = false;
  input.disabled = false;
  form.querySelector("button").disabled = false;
  applyEnvelope(envelope);
  input.focus();
}

async function submitTurn(raw, display) {
  if (gameOver || !sessionId) return;
  const text = (raw || "").trim();
  if (!text) return;
  input.value = "";
  try {
    const envelope = await fetchJSON("/api/turn", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, input: text }),
    });
    applyEnvelope(envelope, display || text);
  } catch (err) {
    addEntry(err.message, "system");
  }
}

function resetToPicker() {
  sessionId = null;
  gameOver = false;
  currentChoices = [];
  play.hidden = true;
  picker.hidden = false;
  newGameBtn.hidden = true;
  endingBanner.hidden = true;
  document.body.dataset.genre = "none";
  document.body.dataset.visual = "boot";
  input.value = "";
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  submitTurn(input.value);
});

newGameBtn.addEventListener("click", resetToPicker);

async function boot() {
  try {
    const genres = await fetchJSON("/api/genres");
    grid.innerHTML = "";
    genres.forEach((genre) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "genre-card";
      btn.innerHTML = `<strong>${genre.title}</strong>`;
      const span = document.createElement("span");
      span.textContent = genre.blurb;
      btn.appendChild(span);
      btn.addEventListener("click", () => {
        startGame(genre.id, genre.title).catch((err) => showError(pickerError, err.message));
      });
      grid.appendChild(btn);
    });
  } catch (err) {
    showError(pickerError, `Cannot reach IF-ENGINE: ${err.message}`);
  }
}

boot();
