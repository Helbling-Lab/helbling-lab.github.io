---
layout: page
title: Research
---



### Delta Arrays
<img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/delta_arrays.jpg" alt="">

<p style="text-align: justify;"> </p>

Dexterous manipulation capabilities of end-effectors afford us a wide range of strategies for fine-grained manipulation tasks. Recent utilization of readily available materials like soft filaments and silicone elastomers has enabled the development of low-cost mechanically intelligent robotic manipulators. This is important for democratizing robot manipulation and increasing accessibility in robotics. However, these robots generally have complex non-linear dynamics that are hard to model analytically, and even harder to learn numerically in the real world in a sample efficient manner. Towards these challenges, we propose a novel manipulator for exploring the capabilities of a complex multi-robot dexterous manipulation system and accessible hardware that can leverage these algorithms to accomplish a wide variety of tasks.

We present an array of 64 linear soft delta robots in an 8x8 hexagonal grid, for the development of new manipulation paradigms that can learn complex prehensile and non-prehensile skills in the real world. The 3D-printed soft TPU links provide mechanical compliance and allow collisions without harming the end-effector. We demonstrate dexterous manipulation capabilities of the delta array using reinforcement learning while leveraging the compliance to not break the end-effectors. Our evaluations show that the resulting 192 DoF-compliant robot is capable of performing various coordinated distributed manipulations of a variety of objects, including translation, alignment, prehensile squeezing, lifting, and grasping.

For more information, please contact [Sarvesh](https://servo97.github.io).

<!-- Check out our CHI 2020 [video presentation](https://youtu.be/ILgJDQSlgYI) to learn more. -->

<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1">
{% include render_pub_list.liquid variable="projects" value="delta_robots" check="contains" %}
</div>
</details>





### Springtail µBot
<!-- <img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/delta_arrays.jpg" alt=""> -->

<p style="text-align: justify;"> </p>
Springtails are tiny arthropods that crawl and jump. They jump by temporarily storing elastic energy in resilin elastic cuticular structures and releasing that energy to accelerate a tail, called a furca, propelling them in the air. We present an autonomous, springtail-inspired microrobot that can crawl and jump. The microrobot has a mass of 980mg and stands 13mm tall, and has on-board sensing, computation, and power, enabling autonomy. The microrobot was designed with a super-elastic shape memory alloy (SMA) spring that is manually loaded to store elastic energy. The on-board sensing and computation triggers an actuator at the jump frequency range that unlatches the spring, launching the microrobot into the air at speeds up to 3.171 m/s. At the same time, the microrobot is capable of crawling, when actuated at frequencies lower or higher than the jump frequency range, demonstrating autonomous multimodal locomotion.


<!-- For more information, please contact [Sarvesh](https://servo97.github.io). -->

<!-- Check out our CHI 2020 [video presentation](https://youtu.be/ILgJDQSlgYI) to learn more. -->

<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1">
{% include render_pub_list.liquid variable="projects" value="springtail" check="contains" %}
</div>
</details>


### DeltaHand
<!-- <img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/delta_arrays.jpg" alt=""> -->

<p style="text-align: justify;"> </p>
DeltaHand is a synergistic robotic hand platform for dexterous manipulation. By leveraging the modularity of Delta robots, our hands are easy to configure to different degrees of freedom with actuation synergies. The manufacturing is low cost by using off-the-shelf materials (the robot can be manufactured in less than a day and costs under $800). We use soft Delta links for the fingers, and show that our hands can compliantly and safely interact with the environment. 

We demonstrate grasping of daily objects using our hand prototypes and teleoperating a 9-actuator Delta hand with a Franka robot arm for dexterous manipulation tasks, we show that we can easily control our hands by leveraging the synergy of our hands while maintaining the necessary dexterity.
<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1">
<!-- {% include render_pub_list.liquid variable="projects" value="delta_robots" check="contains" %} -->
</div>
</details>

<!-- ### Tunable Stiffness
 <img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/Tunable Stiffness Incline.png" alt="">

<p style="text-align: justify;"> </p>

MiniRHex robot, a close design variation of the RHex robot, is a small, open-source,
fully programmable, and cost efficient hexapod robot. Currently, little research has been
conducted on how the materials of the MiniRhex robot legs could impact the
performance of the robot, especially while treading through wet terrain or environments
with high humidity variations.

To fill in this gap, our research focuses on the utilization of an innovative bioplastic
material to improve the performance of the MiniRHex robot in high humidity
environments. Inspired by tree frogs’ ability to adapt to a wet environment, we designed
new legs for MiniRHex using bioplastic which allows the legs to change their stiffness
and traction characteristics with respect to humidity. This capability of the material
opens up new possibilities for the development of MiniRHex robots that are capable of
responding rapidly to changes in their surroundings, especially in wet or slippery
conditions.
<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1"> -->
<!-- {% include render_pub_list.liquid variable="projects" value="delta_robots" check="contains" %} -->
<!-- </div>
</details> -->


<!-- ### Delta Walker -->
 <!-- <img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/Tunable Stiffness Inclie.jpg" alt=""> -->

<!-- <p style="text-align: justify;"> </p>
Delta Walker is a project that stemmed from the Delta Hand, inspired by the Addams Family Hand, Thing. 

We aim to build a walking robot that is small, light, and easy to manufacture. Using linearly-actuated Delta robots with three degrees of freedom, we are investigating the walking gaits that can be created. We are experimenting with coupling link motions between delta robots and usage of a compliant material. Current work is focused on determining the possible gaits in simulation.

<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1"> -->
<!-- {% include render_pub_list.liquid variable="projects" value="delta_robots" check="contains" %} -->
<!-- </div>
</details> -->


### Rescue Rollers
 <!-- <img align="left" width="200" height="200" style="margin:20px 20px" src="/assets/img/research/Rescue Rollers Photo.jpg" alt=""> -->

<p style="text-align: justify;"> </p>
Rescue Rollers are centimeter scale robots designed to operate in unstructured environments. We are exploring how we can achieve robust locomotion with robots of this size after natural disasters. By leveraging their size and a suite of sensing capabilities, a swarm of Rescue Rollers can help first-responders safely and efficiently locate and recover survivors.

Rescue Rollers are also part of a symbiotic system with vine robots. They provide steering and enhanced sensing capabilities, while the vine robots allow for efficient large scale locomotion and power for the centi-robots.
<details>
<summary markdown="1" style="display: list-item;">
<h4 style="display: inline;">Relevant publications</h4>
</summary>
<div markdown="1">
<!-- {% include render_pub_list.liquid variable="projects" value="delta_robots" check="contains" %} -->
</div>
</details>

