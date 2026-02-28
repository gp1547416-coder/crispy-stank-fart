const facts = [
  "A group of cats is called a clowder.",
  "Cats can rotate their ears 180 degrees.",
  "The oldest known pet cat existed 9,500 years ago.",
  "A cat's purr can have calming effects on humans.",
  "Cats have whiskers on the backs of their front legs too.",
];

const button = document.getElementById("factButton");
const fact = document.getElementById("fact");

button?.addEventListener("click", () => {
  const index = Math.floor(Math.random() * facts.length);
  fact.textContent = facts[index];
});
