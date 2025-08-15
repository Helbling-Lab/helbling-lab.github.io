---
layout: page
title: "Researchers"
subtitle: Helbling Lab Researchers
---

<style>
  .researcher-section { margin: 2rem 0 3rem; }
  .researcher-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 18px;
    align-items: start;
  }
  .person-card {
    border: 1px solid #e6e6e6;
    border-radius: 14px;
    padding: 14px;
    background: #fff;
  }
  .person-photo {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 12px;
    border: 1px solid #eee;
    background: #fafafa;
  }
  .person-name { font-weight: 650; font-size: 1.05rem; margin: 10px 0 4px; }
  .person-role { color: #666; font-size: 0.95rem; margin-bottom: 8px; }
  .person-meta { font-size: 0.92rem; line-height: 1.35; }
  .person-meta b { font-weight: 600; }
</style>

{% assign pi = 
  [
    {
      "name":"Elizabeth Farrell Helbling",
      "role":"Principal Investigator",
      "img":"efh.jpg",
    }
  ]
%}

{% assign phd = 
  [
    { "name":"Cameron Urban", "role":"PhD Student",
      "img":"cameron_urban.jpg",
      "major":"Mechanical Engineering",
      "project":"DanioBot"
    },
    { "name":"Julie Villamil", "role":"PhD Student",
      "img":"julie_villamil.jpg",
      "major":"Electrical & Computer Engineering",
      "project":"Crawler Bot" # TODO: PROPER NAME
    },
    { "name":"Harry Gao", "role":"PhD Student",
      "img":"harry_gao.jpg",
      "major":"Mechanial Engineering",
      "project":"GammaBot"
    }
  ]
%}

{% assign masters = 
  [
    { "name":"Cheney Zhang", "role":"Masters of Science Student",
      "img":"cheney_zhang.jpg",
      "major":"Mechanial Engineering",
      "project":"GammaBot"
    }
  ]
%}

{% assign undergrads = 
  [
    { "name":"Jack Long", "role":"Undergraduate Researcher",
      "img":"jack_long.jpg",
      "major":"Mechanical Engineering",
      "project":"Crawler Bot"
    },
    { "name":"Ethan Zhang", "role":"Undergraduate Researcher",
      "img":"ethan_zhang.jpg",
      "major":"Computer Science",
      "project":"GammaBot"
    }
  ]
%}

## PI
<div class="researcher-section researcher-grid">
  {% for p in pi %}
  <div class="person-card">
    <img class="person-photo" src="{{ '/assets/img/headshots/' | append: p.img | relative_url }}" alt="{{ p.name }}">
    <div class="person-name">{{ p.name }}</div>
    <div class="person-role">{{ p.role }}</div>
    <div class="person-meta"><b>Major/Field:</b> {{ p.major }}</div>
    <div class="person-meta"><b>Active project:</b> {{ p.project }}</div>
  </div>
  {% endfor %}
</div>

## PhD Students
<div class="researcher-section researcher-grid">
  {% for p in phd %}
  <div class="person-card">
    <img class="person-photo" src="{{ '/assets/img/headshots/' | append: p.img | relative_url }}" alt="{{ p.name }}">
    <div class="person-name">{{ p.name }}</div>
    <div class="person-role">{{ p.role }}</div>
    <div class="person-meta"><b>Major/Field:</b> {{ p.major }}</div>
    <div class="person-meta"><b>Active project:</b> {{ p.project }}</div>
  </div>
  {% endfor %}
</div>

## Master’s Students
<div class="researcher-section researcher-grid">
  {% for p in masters %}
  <div class="person-card">
    <img class="person-photo" src="{{ '/assets/img/headshots/' | append: p.img | relative_url }}" alt="{{ p.name }}">
    <div class="person-name">{{ p.name }}</div>
    <div class="person-role">{{ p.role }}</div>
    <div class="person-meta"><b>Major/Field:</b> {{ p.major }}</div>
    <div class="person-meta"><b>Active project:</b> {{ p.project }}</div>
  </div>
  {% endfor %}
</div>

## Undergraduate Students
<div class="researcher-section researcher-grid">
  {% for p in undergrads %}
  <div class="person-card">
    <img class="person-photo" src="{{ '/assets/img/headshots/' | append: p.img | relative_url }}" alt="{{ p.name }}">
    <div class="person-name">{{ p.name }}</div>
    <div class="person-role">{{ p.role }}</div>
    <div class="person-meta"><b>Major/Field:</b> {{ p.major }}</div>
    <div class="person-meta"><b>Active project:</b> {{ p.project }}</div>
  </div>
  {% endfor %}
</div>
