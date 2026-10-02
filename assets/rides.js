(function () {
  const rides = window.PARK.rides;
  const bySlug = {};
  rides.forEach(function (ride) {
    bySlug[ride.slug] = ride;
  });

  const index = document.getElementById("ride-index");
  const stage = document.getElementById("ride-stage");
  let current = null;
  let frame = 0;

  function isCaution(text) {
    return /sakıncalıdır/.test(text);
  }

  function renderIndex(active) {
    const groups = [
      ["adult", "Yetişkin Takımları"],
      ["kid", "Çocuk Takımları"],
    ];
    index.innerHTML = groups
      .map(function (group) {
        const buttons = rides
          .filter(function (ride) {
            return ride.group === group[0];
          })
          .map(function (ride) {
            const pressed = ride.slug === active ? ' aria-current="true"' : "";
            return '<li><button type="button" data-slug="' + ride.slug + '"' + pressed + ">" + ride.name + "</button></li>";
          })
          .join("");
        return "<h2>" + group[1] + "</h2><ul>" + buttons + "</ul>";
      })
      .join("");
  }

  function show(slug, push) {
    const ride = bySlug[slug] || bySlug["atli-karinca-9"];
    current = ride;
    frame = 0;
    if (push) history.replaceState(null, "", "#" + ride.slug);
    renderIndex(ride.slug);
    paint();
    const active = index.querySelector('[aria-current="true"]');
    if (active && window.matchMedia("(max-width: 980px)").matches) {
      stage.scrollIntoView({ block: "start" });
    }
  }

  function paint() {
    const ride = current;
    const photo = ride.images[frame] || "";
    const copy = ride.paragraphs
      .map(function (paragraph) {
        const cls = isCaution(paragraph) ? ' class="note"' : "";
        return "<p" + cls + ">" + paragraph + "</p>";
      })
      .join("");
    const thumbs = ride.images
      .map(function (src, i) {
        const on = i === frame ? ' aria-current="true"' : "";
        return '<button type="button" data-frame="' + i + '"' + on + '><img src="' + src + '" alt=""></button>';
      })
      .join("");
    stage.classList.remove("is-switching");
    void stage.offsetWidth;
    stage.classList.add("is-switching");
    stage.innerHTML =
      (photo ? '<img class="stage-photo" src="' + photo + '" alt="' + ride.name + '">' : "") +
      "<h2>" + ride.name + "</h2>" +
      '<div class="prose">' + (copy || "") + "</div>" +
      (ride.images.length > 1 ? '<div class="film">' + thumbs + "</div>" : "") +
      (ride.images.length > 1
        ? '<div class="photo-nav"><button type="button" data-step="-1">Önceki</button><button type="button" data-step="1">Sonraki</button></div>'
        : "");
  }

  index.addEventListener("click", function (event) {
    const button = event.target.closest("button[data-slug]");
    if (!button) return;
    show(button.dataset.slug, true);
  });

  stage.addEventListener("click", function (event) {
    const thumb = event.target.closest("button[data-frame]");
    if (thumb) {
      frame = Number(thumb.dataset.frame);
      paint();
      return;
    }
    const step = event.target.closest("button[data-step]");
    if (!step || !current) return;
    const count = current.images.length;
    frame = (frame + Number(step.dataset.step) + count) % count;
    paint();
  });

  window.addEventListener("hashchange", function () {
    show(location.hash.slice(1), false);
  });

  show(location.hash.slice(1), false);
})();
