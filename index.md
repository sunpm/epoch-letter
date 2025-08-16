---
layout: default
title: 我的未来胶囊
---

<style>
  .capsules { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
  .capsule { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,.05); }
  .capsule h3 { margin: 0 0 8px; font-size: 18px; }
  .capsule .meta { color: #6b7280; font-size: 14px; margin-bottom: 8px; }
  .capsule .content { white-space: pre-wrap; line-height: 1.6; }
  .empty { color: #6b7280; }
</style>

# 我的未来胶囊

{% assign items = site.data.capsules | where: "status", "sent" | where: "display_on_fork", true %}

{% if items and items.size > 0 %}

<div class="capsules">
  {% for c in items %}
  <article class="capsule">
    <h3>{{ c.subject | default: "一封来自过去的信件" }}</h3>
    <div class="meta">寄出日期：{{ c.delivery_date }} · 收件人：{{ c.email }}</div>
    <div class="content">{{ c.content }}</div>
  </article>
  {% endfor %}
  
</div>
{% else %}
<p class="empty">暂无已寄出的胶囊。</p>
{% endif %}

<hr/>
<p class="empty">此页面仅展示我在本仓库中的已发送（sent）胶囊。</p>
