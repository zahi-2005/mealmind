document.addEventListener("DOMContentLoaded", function () {
  console.log("script.js is running!");

  // ----- 1. Instructions click to mark done -----
  const steps = document.querySelectorAll("ol.steps li");
  steps.forEach((step) => {
    step.style.cursor = "pointer";
    step.title = "Click to mark as done";
    step.addEventListener("click", () => {
      if (step.style.textDecoration === "line-through") {
        step.style.textDecoration = "none";
        step.style.opacity = "1";
      } else {
        step.style.textDecoration = "line-through";
        step.style.opacity = "0.6";
      }
    });
  });

  // ----- 2. Ingredients hover → highlight nutrition table row -----
  const ingredientBoxes = document.querySelectorAll(".ingredient-box");
  const tableRows = document.querySelectorAll(".table tbody tr");

  ingredientBoxes.forEach((box, idx) => {
    box.addEventListener("mouseenter", () => {
      if (tableRows[idx]) tableRows[idx].style.background = "#e0f2ff";
    });
    box.addEventListener("mouseleave", () => {
      if (tableRows[idx]) tableRows[idx].style.background = "";
    });
  });

  // ----- 3. Smooth scroll for headings -----
  const headings = document.querySelectorAll("h2.section-title");
  headings.forEach((heading) => {
    heading.style.cursor = "pointer";
    heading.title = "Click to scroll to section";
    heading.addEventListener("click", () => {
      // Determine target based on heading text
      let target;
      const text = heading.textContent.toLowerCase();
      if (text.includes("ingredients")) {
        target = document.querySelector(".ingredients-grid");
      } else if (text.includes("instructions")) {
        target = document.querySelector("ol.steps");
      } else if (text.includes("nutrition")) {
        target = document.querySelector(".table");
      }
      if (target) target.scrollIntoView({ behavior: "smooth" });
    });
  });
});


