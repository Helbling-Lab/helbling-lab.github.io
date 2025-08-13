---
layout: home
title: Helbling Lab @ Cornell
subtitle: Insect-inspired microrobotics
cover-img: ""
---

## About Us

<p style="text-align: justify;"> 
    The Helbling Robotics Lab focuses on designing autonomous insect-scale robotic platforms that can perform sustained, intelligent operation in real-world environments. We focus on holistic design founded in both theory and experiments in which we co-design mechanisms, system architecture, and control with the final environment and task in mind. In the group, this work is divided into two main themes: (1) leveraging cm-scale physics to develop effective locomotion strategies at the insect-scale, and (2) overcoming challenges to design and integrate mm-scale perception, power, and control systems.
</p>

We are a part of the [Electrical and Computer Engineering Department](https://www.ece.cornell.edu/ece) at [Cornell University](https://cornell.edu/). 

If you are looking to join us, [click here](mailto:efh45@cornell.edu).
<!-- We are looking to expand our team. If you're interested, read about our [open positions]()!  -->
To get more information about research and facilities, [click here](/research).

Feel free to stop by our lab in Bard 347 to see our amazing robots in action!

---
#### News
{% for item in site.data.news limit:5 %}
  <div class="news-item">
    {% if item.image %}
      <div class="news-with-image">
        <div class="news-with-image-text">
          <p>{{ item.content }}</p>
          <p><em>{{ item.date }}</em></p>
        </div>
        <img class="news-with-image-image" src="{{ item.image }}" alt="News Image" />
      </div>
    {% else %}
      <div class="news-without-image">
        <p>{{ item.content }}</p>
        <p><em>{{ item.date }}</em></p>
      </div>
    {% endif %}
  </div>
{% endfor %}


<!-- https://www.publicalbum.org/blog/embedding-google-photos-albums -->
<!-- https://photos.app.goo.gl/AYREiQgT7ZPnUuNR9 -->
<script src="https://cdn.jsdelivr.net/npm/publicalbum@latest/embed-ui.min.js" async></script>
<div class="pa-carousel-widget" style="width:100%; height:480px; display:none;"
  data-link="https://photos.app.goo.gl/AYREiQgT7ZPnUuNR9"
  data-title="LabPhotos"
  data-description="9 new items added to shared album"
  data-repeat="false">
  <object data="https://lh3.googleusercontent.com/pw/AP1GczNF7j9d2aIsjzCXlfbVxB3Dp4nPfC3XfNyNRJ8C8_HzabtJMg66Xj8JolLKCbLKPwES3oOHobo4fuEUK2cyfF4wwiMtl0wWeA2JNvHDHpJCZa6l5L9-=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczMYcdgQ2e7j8L1SPNhjO_1yj168dP9Fo6V40Aal-FJ4ffXcMD2bVepVYWD7hKaAJ1M4ulPhTxrSSN0d_QA2oM-aC5BxlW9mSZDclRbf5hGMmVWfpJJX=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczPjPaiZREe1hWyMiIrAx098VgzZUDBhUHWCcFoTxU3dOiRtrOWfm195MOyQKR2fiEHQKuh5_0ctfZchBuq6JQ2kZQL5N7m7cwCm3CF5gY2xO8BCMLGE=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczOBFkb6sOEkcYfI2oNBFTl8aYO6eQLPt8OvK0mo70OC3pB4iI_FEgO21yrHN6hk_kHrPltyN25tkqVPCh0zEsU9mV7ejm7Bu1nEjSoAZCNmXp6H5UJJ=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczOH-crk6M-RKUMVMsYSgsh3GgtiUvSXjYFiFFjEHsVj5zr-WGC-LnsshZxWYaR3d9S5fNoa7A51bSTFAZHc4g7rJCbZ0P2aCmLM9ks1s10He-leL3GB=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczM8gBTOEFtYnuBzjQA85SdWXuaoEMe-KBaevjjxy9VWuit4uLeGl3-bU3gAYes25PBVJ7FbvD-EwSyYSnTiB-3KgvRFJ551PG1VSHmnOCGV26K5IAy4=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczP0kuPJBTzEHcf_OS3FrPl1U_kojCkAXDoICKdCZPs5yXRwzipVaf3JJp4WNOgzeQo0-nJTx4bsOUYB9d88dBQfzBHXcFLPrafAgBN06-qVacaM6yF2=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczMjctTaHF_GnYt_6rjnK-iEnIJLyUxGf17fPe5QTcp3rUSw8Y4VJcOh3tzcl15FzBjYNgnqRwghyBeLxhyEMvhLQd1Fj0bqUYuAUNiDNoV6nmE9VQPB=w1920-h1080"></object>
  <object data="https://lh3.googleusercontent.com/pw/AP1GczMZMBA6YhZMWfTCG4ZGsiwY4vJdtxHnc_JKOM_4SNa649pbJYDJM-EwabqEP13QYhwtqK4rCaLpbhhQhGwIQyQX2LyLJDAoUJiAhFt-HStGL6iJO6jB=w1920-h1080"></object>
</div>

