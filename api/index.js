export default function handler(req, res) {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.status(200).send(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CatWeb Generator</title>
    <style>
      * { box-sizing: border-box; }
      body { margin: 0; font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: linear-gradient(160deg, #f8fafc 0%, #e2e8f0 100%); color: #0f172a; }
      .container { max-width: 760px; margin: 12vh auto; padding: 2rem; border-radius: 1rem; background: white; box-shadow: 0 20px 50px rgba(15, 23, 42, 0.12); }
      button { border: none; border-radius: 0.7rem; padding: 0.7rem 1rem; background: #2563eb; color: white; font-size: 1rem; cursor: pointer; }
      button:hover { background: #1d4ed8; }
      .fact { margin-top: 1rem; padding-left: 1rem; border-left: 4px solid #2563eb; }
      code { background: #0f172a; color: #e2e8f0; padding: 0.25rem 0.4rem; border-radius: 0.3rem; }
    </style>
  </head>
  <body>
    <main class="container">
      <h1>🐱 CatWeb Generator</h1>
      <p>Your Vercel deployment is live.</p>
      <p>Generate a project with <code>python3 catweb_generator.py my-catweb</code>.</p>
      <button id="factButton">Show Cat Fact</button>
      <blockquote id="fact" class="fact">Cats sleep 12–16 hours a day.</blockquote>
    </main>
    <script>
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
    </script>
  </body>
</html>`);
}
