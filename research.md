---
layout: page
title: Research
---

<!-- Publications button -->
<div style="text-align:center; margin: 0 0 24px 0;">
  <a href="https://scholar.google.com/citations?user=Pwd7hJYAAAAJ&hl=en" target="_blank" rel="noopener"
     style="display:inline-block;padding:10px 14px;border-radius:8px;border:1px solid #ddd;text-decoration:none;">
    🔎 View current publications on Google Scholar
  </a>
</div>

<style>
  .project { display:flex; gap:20px; align-items:center; margin:24px 0 40px; }
  .project.right { flex-direction: row-reverse; }
  .project .img {
    flex: 0 0 220px;
    height: 220px;
    background: #f3f3f3;
    border: 1px solid #e6e6e6;
    border-radius: 8px;
    display:flex; align-items:center; justify-content:center;
    color:#777; font-size:0.9rem; text-align:center; padding:10px;
  }
  .project .body h3 { margin: 0 0 6px 0; }
  .project .meta { color:#555; font-size:0.95rem; margin-bottom:6px; }
</style>



<!-- # Recent Publications

{% for pub in site.data.pubs %}
  <div class="publication" style="margin-bottom: 1.5em;">
    <strong>{{ pub.title }}</strong><br>
    <span>{{ pub.authors }}</span>
    {% if pub.venue %}<span> | {{ pub.venue }}</span>{% endif %}
    {% if pub.year %}<span> ({{ pub.year }})</span>{% endif %}
    {% if pub.description %}
      <div style="margin: 0.5em 0; color: #555;">{{ pub.description }}</div>
    {% endif %}
    <div>
      {% if pub.scholar_link %}
        {% if pub.link %} &nbsp;|&nbsp; {% endif %}
        <a href="{{ pub.scholar_link }}" target="_blank">Google Scholar</a>
      {% endif %}
    </div>
  </div>
{% endfor %} -->



<!-- ========== 1. GammaBot ========== -->


<div class="project left">
  <div class="img">
  coming soon!
    <!-- <img src="{{ '/assets/img/research/gammabot_smaller.jpeg' | relative_url }}" alt="GammaBot"
         style="width:100%;height:100%;object-fit:cover;border-radius:8px;"> -->
    
  </div>
  <div class="body">
    <h3>GammaBot</h3>
    <div class="meta">Lead: <strong>Harry Gao</strong></div>
    <p>A surface-skimming robot inspired by water striders, leveraging surface tension to stay afloat and small wings for propulsion. Weighs &lt; 1&nbsp;g.</p>
  </div>
</div>


<!-- ========== 2. Daniobot (image right) ========== -->
<div class="project right">
  <div class="img">

  coming soon!
    <!-- <img src="{{ './assets/img/research/Daniobot.jpg' | relative_url }}" alt="Daniobot"
         style="width:100%;height:100%;object-fit:cover;border-radius:8px;">  -->
  </div>
  <div class="body">
    <h3>Daniobot</h3>
    <div class="meta">Lead: <strong>Cameron Urban</strong></div>
    <p>A fish-inspired microrobot that maneuvers into tight underwater spaces. Self-contained and powered, &lt; 1&nbsp;g total mass.</p>
  </div>
</div>

<!-- ========== 3. COMT ========== -->
<div class="project left">
  <div class="img">
  coming soon!
<!-- 
    <img src="{{ '/assets/img/research/COMT.png' | relative_url }}" alt="COMT"
         style="width:100%;height:100%;object-fit:cover;border-radius:8px;"> -->
    
  </div>
  <div class="body">
    <h3>COMT</h3>
    <div class="meta">Lead: <strong>Julie Villamil</strong></div>
    <p>A lightweight land-roaming crawler for robust ground locomotion at small scales.</p>
  </div>
</div> 
