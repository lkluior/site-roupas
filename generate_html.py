import os

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="STREET VIBE - Seu estilo, sua identidade. Catálogo de streetwear.">
    <title>STREET VIBE | Streetwear & Moda</title>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="header">
        <div class="container header-container">
            <a href="#" class="logo">STREET<span>VIBE</span></a>
            <nav class="nav-menu">
                <ul class="nav-links">
                    <li><a href="#inicio" class="nav-link">Início</a></li>
                    <li><a href="#roupas" class="nav-link">Roupas</a></li>
                    <li><a href="#marcas" class="nav-link">Marcas</a></li>
                    <li><a href="#galeria" class="nav-link">Galeria</a></li>
                    <li><a href="#contato" class="nav-link">Contato</a></li>
                </ul>
            </nav>
            <a href="#" class="btn btn-primary btn-whatsapp-header whatsapp-btn">Falar no WhatsApp</a>
            <button class="menu-toggle hamburger" aria-label="Abrir menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <main>
        <!-- Seção Hero -->
        <section id="inicio" class="hero">
            <div class="hero-bg"></div>
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1 class="hero-title">Seu estilo. Sua identidade.</h1>
                <p class="hero-subtitle">Descubra peças selecionadas para transformar seu estilo.</p>
                <div class="hero-buttons">
                    <a href="#roupas" class="btn btn-primary">Ver Roupas</a>
                    <a href="#" class="btn btn-outline btn-whatsapp whatsapp-btn">Falar no WhatsApp</a>
                </div>
            </div>
        </section>

        <!-- Seção Carrossel (Substitua as imagens aqui) -->
        <section class="carousel-section">
            <div class="carousel-container">
                <div class="carousel-track">
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600" alt="Carrossel" loading="lazy"></div>
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1607522370275-f14206abe190?w=600" alt="Carrossel" loading="lazy"></div>
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=600" alt="Carrossel" loading="lazy"></div>
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600" alt="Carrossel" loading="lazy"></div>
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600" alt="Carrossel" loading="lazy"></div>
                    <div class="carousel-item"><img src="https://images.unsplash.com/photo-1588850561407-ed78c334e67a?w=600" alt="Carrossel" loading="lazy"></div>
                </div>
            </div>
        </section>

        <!-- Seção de Filtro por Marcas -->
        <section id="marcas" class="filter-section reveal">
            <div class="container">
                <h2 class="section-title">Encontre seu estilo</h2>
                <div class="filter-container">
                    <button class="filter-btn active" data-brand="Todas">Todas</button>
                    <button class="filter-btn" data-brand="Nike">Nike</button>
                    <button class="filter-btn" data-brand="Adidas">Adidas</button>
                    <button class="filter-btn" data-brand="Puma">Puma</button>
                    <button class="filter-btn" data-brand="Vans">Vans</button>
                    <button class="filter-btn" data-brand="Jordan">Jordan</button>
                </div>
            </div>
        </section>

        <!-- Seção Catálogo de Roupas -->
        <section id="roupas" class="catalog-section reveal">
            <div class="container">
                <div class="product-grid products-grid">
                    
                    <!-- PRODUTO 1 -->
                    <article class="product-card" data-brand="Nike">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600" alt="Conjunto Summer Vibes" class="product-img" loading="lazy">
                            <span class="product-tag">Nike</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Conjunto</div>
                            <h3 class="product-name">Conjunto Summer Vibes</h3>
                            <p class="product-desc">Conjunto de camisa leve e short confortável para o verão.</p>
                            <div class="product-meta">
                                <span>Cor: Preto/Branco</span>
                                <span>Tamanhos: P, M, G, GG</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Conjunto Summer Vibes">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 2 -->
                    <article class="product-card" data-brand="Adidas">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600" alt="Conjunto Street Classic" class="product-img" loading="lazy">
                            <span class="product-tag">Adidas</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Conjunto</div>
                            <h3 class="product-name">Conjunto Street Classic</h3>
                            <p class="product-desc">Camisa e short com design clássico das três listras.</p>
                            <div class="product-meta">
                                <span>Cor: Branco/Preto</span>
                                <span>Tamanhos: P, M, G</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Conjunto Street Classic">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 3 -->
                    <article class="product-card" data-brand="Puma">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=600" alt="Conjunto Urban" class="product-img" loading="lazy">
                            <span class="product-tag">Puma</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Conjunto</div>
                            <h3 class="product-name">Conjunto Urban</h3>
                            <p class="product-desc">Visual moderno e despojado para o dia a dia.</p>
                            <div class="product-meta">
                                <span>Cor: Bege/Verde</span>
                                <span>Tamanhos: M, G, GG</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Conjunto Urban">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 4 -->
                    <article class="product-card" data-brand="Nike">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=600" alt="Camisa Logo Box" class="product-img" loading="lazy">
                            <span class="product-tag">Nike</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Camisa</div>
                            <h3 class="product-name">Camisa Logo Box</h3>
                            <p class="product-desc">Camisa de algodão premium com logo minimalista.</p>
                            <div class="product-meta">
                                <span>Cor: Branco</span>
                                <span>Tamanhos: P, M, G, GG</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Camisa Logo Box">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 5 -->
                    <article class="product-card" data-brand="Vans">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1622445275576-721325763afe?w=600" alt="Camisa Oversized" class="product-img" loading="lazy">
                            <span class="product-tag">Vans</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Camisa</div>
                            <h3 class="product-name">Camisa Oversized</h3>
                            <p class="product-desc">Corte largo e despojado para máximo conforto.</p>
                            <div class="product-meta">
                                <span>Cor: Branco</span>
                                <span>Tamanhos: M, G, GG</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Camisa Oversized">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 6 -->
                    <article class="product-card" data-brand="Jordan">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9?w=600" alt="Camisa Graphic" class="product-img" loading="lazy">
                            <span class="product-tag">Jordan</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Camisa</div>
                            <h3 class="product-name">Camisa Graphic</h3>
                            <p class="product-desc">Estampa exclusiva para compor um visual autêntico.</p>
                            <div class="product-meta">
                                <span>Cor: Preto</span>
                                <span>Tamanhos: P, M, G</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Camisa Graphic">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 7 -->
                    <article class="product-card" data-brand="Adidas">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600" alt="Short Sport Mesh" class="product-img" loading="lazy">
                            <span class="product-tag">Adidas</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Short</div>
                            <h3 class="product-name">Short Sport Mesh</h3>
                            <p class="product-desc">Tecido respirável ideal para dias quentes.</p>
                            <div class="product-meta">
                                <span>Cor: Preto</span>
                                <span>Tamanhos: P, M, G, GG</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Short Sport Mesh">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 8 -->
                    <article class="product-card" data-brand="Puma">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1565084888279-aca607fccece?w=600" alt="Short Cargo Casual" class="product-img" loading="lazy">
                            <span class="product-tag">Puma</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Short</div>
                            <h3 class="product-name">Short Cargo Casual</h3>
                            <p class="product-desc">Bolsos utilitários e modelagem confortável.</p>
                            <div class="product-meta">
                                <span>Cor: Verde Militar</span>
                                <span>Tamanhos: 38 ao 44</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Short Cargo Casual">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 9 -->
                    <article class="product-card" data-brand="Nike">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600" alt="Short Moletom Comfort" class="product-img" loading="lazy">
                            <span class="product-tag">Nike</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Short</div>
                            <h3 class="product-name">Short Moletom Comfort</h3>
                            <p class="product-desc">O conforto do moletom em um short estiloso.</p>
                            <div class="product-meta">
                                <span>Cor: Cinza</span>
                                <span>Tamanhos: P, M, G</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Short Moletom Comfort">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 10 -->
                    <article class="product-card" data-brand="Vans">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1514327605112-b887c0e61c0a?w=600" alt="Bucket Hat Classic" class="product-img" loading="lazy">
                            <span class="product-tag">Vans</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Chapéu</div>
                            <h3 class="product-name">Bucket Hat Classic</h3>
                            <p class="product-desc">Chapéu bucket estiloso para completar o visual.</p>
                            <div class="product-meta">
                                <span>Cor: Preto</span>
                                <span>Tamanho: Único</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Bucket Hat Classic">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 11 -->
                    <article class="product-card" data-brand="Jordan">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1588850561407-ed78c334e67a?w=600" alt="Boné Snapback Heritage" class="product-img" loading="lazy">
                            <span class="product-tag">Jordan</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Chapéu</div>
                            <h3 class="product-name">Boné Snapback Heritage</h3>
                            <p class="product-desc">O clássico snapback com a logo bordada.</p>
                            <div class="product-meta">
                                <span>Cor: Preto/Vermelho</span>
                                <span>Tamanho: Único</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Boné Snapback Heritage">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                    <!-- PRODUTO 12 -->
                    <article class="product-card" data-brand="Adidas">
                        <div class="product-image-container">
                            <img src="https://images.unsplash.com/photo-1521369909029-2afed882baee?w=600" alt="Gorro Beanie" class="product-img" loading="lazy">
                            <span class="product-tag">Adidas</span>
                        </div>
                        <div class="product-details">
                            <div class="product-category">Chapéu</div>
                            <h3 class="product-name">Gorro Beanie</h3>
                            <p class="product-desc">Gorro clássico para dias mais frios.</p>
                            <div class="product-meta">
                                <span>Cor: Mostarda</span>
                                <span>Tamanho: Único</span>
                            </div>
                            <button class="btn btn-primary product-btn whatsapp-btn" data-product="Gorro Beanie">
                                Tenho Interesse
                            </button>
                        </div>
                    </article>

                </div>
            </div>
        </section>

        <!-- Seção Destaques (Opcional - Pode substituir as imagens) -->
        <section class="highlights-section reveal">
            <div class="container">
                <h2 class="section-title" style="color: white; margin-bottom: 30px;">Destaques</h2>
                <div class="highlights-grid">
                    <div class="highlight-card">
                        <img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800" class="highlight-img" alt="Destaque" loading="lazy">
                        <div class="highlight-overlay">
                            <span class="product-tag">Coleção Verão</span>
                            <h3 class="highlight-title">Conjuntos Leves</h3>
                            <button class="btn btn-primary whatsapp-btn" data-product="Coleção Verão">Ver Mais</button>
                        </div>
                    </div>
                    <div class="highlight-card">
                        <img src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=800" class="highlight-img" alt="Destaque" loading="lazy">
                        <div class="highlight-overlay">
                            <span class="product-tag">Exclusivo</span>
                            <h3 class="highlight-title">Streetwear Classic</h3>
                            <button class="btn btn-primary whatsapp-btn" data-product="Streetwear Classic">Ver Mais</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Seção Galeria (Substitua as imagens aqui) -->
        <section id="galeria" class="gallery-section reveal">
            <div class="container">
                <h2 class="section-title">Nossa Coleção</h2>
                <div class="gallery-grid">
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1523398002811-999ca8dec234?w=800" alt="Galeria" loading="lazy"></div>
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800" alt="Galeria" loading="lazy"></div>
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800" alt="Galeria" loading="lazy"></div>
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=800" alt="Galeria" loading="lazy"></div>
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1581044777550-4cfa60707998?w=800" alt="Galeria" loading="lazy"></div>
                    <div class="gallery-item"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=800" alt="Galeria" loading="lazy"></div>
                </div>
            </div>
        </section>

        <!-- Seção de Contato -->
        <section id="contato" class="contact-section reveal section-padding">
            <div class="container text-center">
                <h2>Vamos conversar?</h2>
                <p style="margin-bottom: 20px;">Entre em contato pelo WhatsApp e tire suas dúvidas</p>
                <a href="#" class="btn btn-primary btn-whatsapp whatsapp-btn">Falar no WhatsApp</a>
            </div>
        </section>
    </main>

    <!-- Modal Lightbox (Galeria) -->
    <dialog id="lightbox" class="lightbox-modal">
        <div class="lightbox-content">
            <button class="lightbox-close" aria-label="Fechar">&times;</button>
            <button class="lightbox-prev" aria-label="Imagem anterior">&#10094;</button>
            <img src="" alt="Imagem ampliada da galeria" id="lightbox-img" class="lightbox-img">
            <button class="lightbox-next" aria-label="Próxima imagem">&#10095;</button>
        </div>
    </dialog>

    <!-- Rodapé -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="#" class="logo">STREET<span>VIBE</span></a>
                    <p style="margin-top: 15px;">Sua loja exclusiva de moda streetwear.</p>
                </div>
                <div class="footer-col">
                    <h3>Links Rápidos</h3>
                    <ul style="margin-top: 15px;">
                        <li><a href="#inicio">Início</a></li>
                        <li><a href="#roupas">Roupas</a></li>
                        <li><a href="#marcas">Marcas</a></li>
                        <li><a href="#galeria">Galeria</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Contato</h3>
                    <ul style="margin-top: 15px;">
                        <li><a href="#" class="whatsapp-btn">WhatsApp</a></li>
                        <li><span>Instagram: @streetvibe</span></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom text-center">
            <br>
            <p>&copy; 2024 STREET VIBE. Todos os direitos reservados.</p>
        </div>
    </footer>

    <!-- Botão Flutuante WhatsApp -->
    <a href="#" class="whatsapp-float whatsapp-btn" aria-label="Conversar no WhatsApp" id="whatsapp-float">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="24" height="24" fill="currentColor"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zM223.9 413.3c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 334.4l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184-186.6 184zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7 .9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg>
    </a>

    <script src="js/script.js" defer></script>
</body>
</html>
"""

with open(r'c:\Users\luka\Desktop\site de roupas\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
