const header = document.querySelector(".site-header");
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".nav");

if (header) {
  const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 12);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

const backdrop = document.createElement("div");
backdrop.className = "nav-backdrop";
if (header && nav) header.insertBefore(backdrop, nav);

document.querySelectorAll(".drop").forEach((drop) => {
  const link = drop.querySelector(":scope > a");
  const panel = drop.querySelector(".drop-panel");
  if (!link || !panel) return;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "drop-toggle";
  button.setAttribute("aria-expanded", "false");
  button.setAttribute("aria-label", link.textContent.trim());
  link.after(button);
  button.addEventListener("click", () => {
    const open = drop.classList.toggle("open");
    button.setAttribute("aria-expanded", open ? "true" : "false");
  });
});

function setMenu(open) {
  if (!nav || !toggle) return;
  nav.classList.toggle("open", open);
  backdrop.classList.toggle("show", open);
  toggle.setAttribute("aria-expanded", open ? "true" : "false");
  document.body.classList.toggle("nav-lock", open);
  const mobile = window.matchMedia("(max-width: 980px)").matches;
  nav.inert = mobile && !open;
}

if (toggle && nav) {
  setMenu(false);
  toggle.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
  backdrop.addEventListener("click", () => setMenu(false));
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.matchMedia("(max-width: 980px)").matches) setMenu(false);
    });
  });
  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMenu(false);
  });
  window.addEventListener("resize", () => {
    if (!window.matchMedia("(max-width: 980px)").matches) setMenu(false);
  });
}

document.querySelectorAll("[data-gallery]").forEach((gallery) => {
  const main = gallery.querySelector("[data-main]");
  const buttons = [...gallery.querySelectorAll("[data-src]")];
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      main.src = button.dataset.src;
      main.alt = button.dataset.alt || "";
      buttons.forEach((item) => item.setAttribute("aria-current", item === button ? "true" : "false"));
    });
  });
});

document.querySelectorAll("[data-contact]").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const note = form.querySelector(".note");
    if (note) note.textContent = form.dataset.done || "Mesajınız alındı.";
    form.reset();
  });
});
