---
layout: page
title: Tags
permalink: /tags
---

{% assign tag_names = "" | split: "|"  %}

{% for posts_by_tag in site.tags %}
  {% assign tag_names = tag_names | push: posts_by_tag.first %}
{% endfor %}

{% assign tag_names = tag_names | sort %}

{% include tag_cloud.html tag_names=tag_names %}

<hr>

<section class="posts-by-tags">
  {% for tag_name in tag_names %}
    <div>
      <h3 id="{{ tag_name }}">
        {{ tag_name | capitalize | replace: "_", " " }}
      </h3>

      {% for post in site.tags[tag_name] %}
        <li><a href="{{ post.url | prepend: baseurl }}">
          {{ post.title }}
        </a></li>
      {% endfor %}
    </div>
  {% endfor %}
</section>