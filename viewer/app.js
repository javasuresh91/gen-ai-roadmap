const TAGS = { pdf: "PDF", notebook: "NB", python: "PY" };
const treeEl = document.getElementById("tree");
const viewer = document.getElementById("viewer");
const sidebar = document.getElementById("sidebar");
let files = [];

function buildTree(list) {
  const root = { dirs: {}, files: [] };
  for (const f of list) {
    const parts = f.path.split("/");
    let node = root;
    for (const dir of parts.slice(0, -1)) {
      node = node.dirs[dir] ??= { dirs: {}, files: [] };
    }
    node.files.push(f);
  }
  return root;
}

function renderNode(node, open) {
  const frag = document.createDocumentFragment();
  const byName = (a, b) => a.localeCompare(b, undefined, { numeric: true });
  for (const name of Object.keys(node.dirs).sort(byName)) {
    const d = document.createElement("details");
    d.open = open;
    const s = document.createElement("summary");
    s.textContent = name;
    const c = document.createElement("div");
    c.className = "children";
    c.appendChild(renderNode(node.dirs[name], open));
    d.append(s, c);
    frag.appendChild(d);
  }
  for (const f of node.files.sort((a, b) => byName(a.name, b.name))) {
    const a = document.createElement("a");
    a.href = "#" + encodeURIComponent(f.path);
    a.dataset.path = f.path;
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = TAGS[f.type];
    const label = document.createElement("span");
    label.textContent = f.name;
    a.append(tag, label);
    frag.appendChild(a);
  }
  return frag;
}

function renderTree(list, open = true) {
  treeEl.replaceChildren(renderNode(buildTree(list), open));
  highlightActive();
}

function highlightActive() {
  const current = decodeURIComponent(location.hash.slice(1));
  treeEl.querySelectorAll("a").forEach(a =>
    a.classList.toggle("active", a.dataset.path === current));
}

function filebar(file) {
  const bar = document.createElement("div");
  bar.className = "filebar";
  const title = document.createElement("span");
  title.textContent = file.path;
  const actions = document.createElement("div");
  actions.className = "actions";
  const open = document.createElement("a");
  open.href = file.url;
  open.target = "_blank";
  open.rel = "noopener";
  open.textContent = "Open in new tab";
  actions.appendChild(open);
  bar.append(title, actions);
  return { bar, actions };
}

async function show(path) {
  const file = files.find(f => f.path === path);
  if (!file) return;
  highlightActive();
  sidebar.classList.remove("open");
  const { bar, actions } = filebar(file);
  viewer.replaceChildren(bar);

  if (file.type === "python") {
    const res = await fetch(file.url);
    const text = await res.text();
    const pre = document.createElement("pre");
    const code = document.createElement("code");
    code.className = "language-python";
    code.textContent = text;
    pre.appendChild(code);
    hljs.highlightElement(code);
    const copy = document.createElement("button");
    copy.textContent = "Copy";
    copy.onclick = async () => {
      await navigator.clipboard.writeText(text);
      copy.textContent = "Copied";
      setTimeout(() => (copy.textContent = "Copy"), 1500);
    };
    actions.prepend(copy);
    viewer.appendChild(pre);
  } else {
    const frame = document.createElement("iframe");
    frame.src = file.url;
    frame.title = file.name;
    viewer.appendChild(frame);
  }
}

function route() {
  const path = decodeURIComponent(location.hash.slice(1));
  if (path) show(path);
}

document.getElementById("search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  if (!q) return renderTree(files, true);
  renderTree(files.filter(f => f.path.toLowerCase().includes(q)), true);
});
document.getElementById("menu").onclick = () => sidebar.classList.toggle("open");
window.addEventListener("hashchange", route);

fetch("files.json")
  .then(r => r.json())
  .then(list => { files = list; renderTree(files); route(); })
  .catch(() => { treeEl.textContent = "Could not load files.json"; });
