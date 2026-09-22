# Manutenção do Site - Just Fast Technologies

## Links Importantes

| O que | Link |
|-------|------|
| Site ao vivo | https://justfast.com.br |
| GitHub (código) | https://github.com/joelfelipe338/justfast-site |
| Google Search Console | https://search.google.com/search-console |
| EmailJS (formulário) | https://www.emailjs.com |
| Hostinger (hospedagem) | https://www.hostinger.com.br |

---

## Tarefas Semanais

- [ ] Verificar o **Search Console** para erros de rastreamento
- [ ] Publicar **1-2 posts** no blog (ver seção abaixo)
- [ ] Compartilhar cada post novo no **LinkedIn**

## Tarefas Mensais

- [ ] Verificar aba **"Desempenho"** no Search Console (quais termos trazem visitantes)
- [ ] Verificar se o **formulário de contato** está funcionando (enviar teste)
- [ ] Atualizar preços no site se necessário

---

## Como Criar um Novo Post no Blog

### 1. Criar o arquivo HTML

Copie um post existente (ex: `blog/quanto-custa-criar-site.html`) e salve com novo nome:
- Use nome descritivo: `blog/nome-do-tema.html`
- Sem acentos, sem espaços, tudo minúsculo, separado por hífen

### 2. Editar o conteúdo

No arquivo copiado, altere:
- `<title>` — Título do post (máx 60 caracteres)
- `<meta name="description">` — Resumo (máx 160 caracteres)
- `<meta name="keywords">` — Palavras-chave separadas por vírgula
- `<link rel="canonical">` — URL completa do novo post
- Tags `hreflang` — Atualizar URLs
- Open Graph (`og:title`, `og:description`, `og:url`) — Atualizar
- Twitter Card — Atualizar título e descrição
- JSON-LD (structured data) — Atualizar headline, description, URL, datas
- Conteúdo do `<article>` — Escrever em PT, EN e ES usando `data-pt`, `data-en`, `data-es`
- Data de publicação

### 3. Adicionar card no blog.html

Abrir `blog.html` e adicionar um novo `<a class="blog-card">` dentro de `.blog-grid`:

```html
<a href="blog/nome-do-tema.html" class="blog-card">
    <span class="blog-card-tag" data-pt="Categoria" data-en="Category" data-es="Categoría">Category</span>
    <h2 data-pt="Título em PT" data-en="Title in EN" data-es="Título en ES">Title in EN</h2>
    <p data-pt="Descrição PT" data-en="Description EN" data-es="Descripción ES">Description EN</p>
    <div class="blog-card-footer">
        <span class="blog-card-date">DD Mês AAAA</span>
        <span class="blog-card-read" data-pt="Ler artigo →" data-en="Read article →" data-es="Leer artículo →">Read article →</span>
    </div>
</a>
```

### 4. Adicionar no sitemap.xml

Adicionar antes do `</urlset>`:

```xml
<url>
    <loc>https://justfast.com.br/blog/nome-do-tema.html</loc>
    <lastmod>AAAA-MM-DD</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
</url>
```

### 5. Publicar

```bash
git add blog/nome-do-tema.html blog.html sitemap.xml
git commit -m "Adiciona post: Nome do Tema"
git push origin main
```

### 6. Solicitar indexação

- Ir no Google Search Console
- Colar a URL do novo post na barra "Inspeção de URL"
- Clicar em "Solicitar indexação"

---

## Como Divulgar no LinkedIn

### Modelo de Post para LinkedIn

```
[Emoji relevante] Novo artigo no blog da Just Fast!

[Título do artigo]

[2-3 frases resumindo o que o leitor vai aprender]

Confira o artigo completo:
[link do post]

#DesenvolvimentoWeb #Tecnologia #JustFast #InteligenciaArtificial #Apps
```

### Exemplo:

```
🚀 Novo artigo no blog da Just Fast!

Quanto Custa Criar um Site Profissional em 2026?

Muita gente quer ter um site mas não sabe quanto investir.
Nesse artigo, comparamos preços de landing pages, sites institucionais,
e-commerces e sistemas web para você tomar a melhor decisão.

Confira o artigo completo:
https://justfast.com.br/blog/quanto-custa-criar-site.html

#DesenvolvimentoWeb #CriarSite #Tecnologia #JustFast #WebDesign
```

### Dicas para o LinkedIn:
- Poste entre **8h-10h** ou **17h-19h** (horários de maior alcance)
- Use **3-5 hashtags** relevantes
- Marque pessoas ou empresas se o post mencionar algum caso
- Responda todos os comentários para aumentar o alcance
- Poste o artigo **no mesmo dia** que publicar no blog

---

## Ideias de Novos Posts

1. "Como escolher uma empresa de desenvolvimento de software"
2. "Quanto tempo demora para criar um aplicativo?"
3. "Site próprio vs só redes sociais: qual a melhor estratégia?"
4. "5 sinais de que sua empresa precisa de um sistema personalizado"
5. "Como a automação pode reduzir custos no seu negócio"
6. "PWA vs App Nativo: qual a diferença e quando usar cada um"
7. "O que é SaaS e como criar um produto digital"
8. "Como a IA está transformando o atendimento ao cliente"
9. "Landing page que converte: o que não pode faltar"
10. "Manutenção de site: por que é essencial e quanto custa"

---

## Pendência: EmailJS

Para o tipo de serviço aparecer nos emails recebidos:
1. Acesse https://www.emailjs.com e faça login
2. Vá em **Email Templates**
3. Edite o template usado no formulário
4. Adicione `{{service}}` onde quiser que o serviço apareça (ex: no corpo do email)
5. Salve o template
