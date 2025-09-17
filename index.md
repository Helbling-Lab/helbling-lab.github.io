---
layout: home
title: Helbling Lab @ Cornell
subtitle: Insect-Inspired Microrobotics
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
