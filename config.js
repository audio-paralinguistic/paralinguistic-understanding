// ParA-LLM project page — siteConfig for optional future templating
const siteConfig = {
  paper: {
    title: "ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding",
    shortTitle: "ParA-LLM",
    authors: [
      { name: "Anonymous", isEqual: true, isCorresponding: false }
    ],
    institution: "Interspeech 2026 (anonymous review)",
    venue: "Interspeech 2026",
    year: "2026",
    status: "submitted",
    links: {
      paper: "#",
      code: null,
      projectPage: null
    }
  }
};
if (typeof window !== "undefined") window.siteConfig = siteConfig;
if (typeof module !== "undefined" && module.exports) module.exports = siteConfig;
