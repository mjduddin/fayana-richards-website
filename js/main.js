/* Dr. Fayana Richards portfolio — site behavior.
   Mobile menu, Selected Work filters, contact form validation, footer year. */

(function () {
  "use strict";

  /* Footer year ---------------------------------------------------------- */
  var yearEl = document.getElementById("footer-year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* Mobile menu ----------------------------------------------------------- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("primary-navigation");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        toggle.focus();
      }
    });
  }

  /* Selected Work filters --------------------------------------------------- */
  var filterGroup = document.querySelector("[data-filter-group]");
  var workCards = document.querySelectorAll("[data-tags]");
  var filterStatus = document.getElementById("filter-status");

  if (filterGroup && workCards.length) {
    filterGroup.addEventListener("click", function (event) {
      var button = event.target.closest(".filter-btn");
      if (!button) return;

      filterGroup.querySelectorAll(".filter-btn").forEach(function (b) {
        b.setAttribute("aria-pressed", String(b === button));
      });

      var filter = button.getAttribute("data-filter");
      var shown = 0;

      workCards.forEach(function (card) {
        var tags = (card.getAttribute("data-tags") || "").split(/\s+/);
        var match = filter === "all" || tags.indexOf(filter) !== -1;
        card.hidden = !match;
        if (match) shown += 1;
      });

      if (filterStatus) {
        var label = button.textContent.trim();
        filterStatus.textContent =
          filter === "all"
            ? "Showing all " + shown + " projects."
            : "Showing " + shown + " project" + (shown === 1 ? "" : "s") + " tagged " + label + ".";
      }
    });
  }

  /* Contact form validation ---------------------------------------------------- */
  var form = document.getElementById("contact-form");

  if (form) {
    var statusEl = document.getElementById("form-status");

    var fields = [
      { id: "name", message: "Please enter your name." },
      { id: "email", message: "Please enter a valid email address." },
      { id: "subject", message: "Please enter a subject." },
      { id: "inquiry-type", message: "Please select an inquiry type." },
      { id: "message", message: "Please enter a message." }
    ];

    function validateField(field) {
      var input = document.getElementById(field.id);
      var error = document.getElementById(field.id + "-error");
      if (!input || !error) return true;

      var value = input.value.trim();
      var valid = value.length > 0;

      if (field.id === "email" && valid) {
        valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
      }

      input.setAttribute("aria-invalid", String(!valid));
      error.textContent = valid ? "" : field.message;
      error.classList.toggle("is-visible", !valid);
      return valid;
    }

    fields.forEach(function (field) {
      var input = document.getElementById(field.id);
      if (input) {
        input.addEventListener("blur", function () {
          validateField(field);
        });
      }
    });

    form.addEventListener("submit", function (event) {
      var allValid = true;
      var firstInvalid = null;

      fields.forEach(function (field) {
        var valid = validateField(field);
        if (!valid && !firstInvalid) {
          firstInvalid = document.getElementById(field.id);
        }
        allValid = allValid && valid;
      });

      if (!allValid) {
        event.preventDefault();
        if (statusEl) {
          statusEl.className = "form-status is-error";
          statusEl.textContent =
            "The form has not been sent yet. Please correct the highlighted fields and try again.";
        }
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      /* Success messaging:
         - Netlify Forms redirects to /contact/?submitted=true (configured on the form).
         - Formspree can redirect with the _next hidden field.
         The confirmation message below is shown when the page loads with ?submitted=true. */
    });

    if (window.location.search.indexOf("submitted=true") !== -1 && statusEl) {
      statusEl.className = "form-status is-success";
      statusEl.textContent =
        "Thank you. Your message has been sent, and Fayana will respond as soon as possible.";
      statusEl.focus && statusEl.focus();
    }
  }
})();
