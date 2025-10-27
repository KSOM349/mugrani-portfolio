from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# الترجمة للغات المختلفة
translations = {
    'ar': {
        'title': 'مقراني وجرف',
        'home': 'الرئيسية',
        'services': 'الخدمات', 
        'projects': 'المشاريع',
        'contact': 'اتصل بنا',
        'welcome': 'مرحبا بكم في مقراني وجرف',
        'tagline': 'شركة رائدة في مجال التقنية والابتكار',
        'slogan': 'نحو مستقبل تقني متقدم',
        'our_services': 'خدماتنا المتكاملة',
        'tech': 'التقنية',
        'tech_desc': 'هندسة الشبكات - تصميم وتركيب شبكات الحاسب والاتصالات',
        'maintenance': 'تشغيل وصيانة',
        'maintenance_desc': 'صيانة وتشغيل الأنظمة التقنية',
        'construction': 'البناء',
        'construction_desc': 'تركيب الأرضيات - تركيب جميع أنواع الأرضيات باحترافية',
        'carpet': 'تركيب السجاد',
        'carpet_desc': 'تركيب السجاد بأنواعه المختلفة',
        'consulting': 'إرشادات البناء',
        'consulting_desc': 'استشارات بناء من ذوي الخبرة',
        'switch_arabic': 'العربية',
        'switch_swedish': 'Svenska',
        'switch_english': 'English'
    },
    'sv': {
        'title': 'Mugrani & Djerf Ab',
        'home': 'Hem',
        'services': 'Tjänster',
        'projects': 'Projekt',
        'contact': 'Kontakt',
        'welcome': 'Välkommen till Mugrani & Djerf',
        'tagline': 'Ett ledande företag inom teknik och innovation',
        'slogan': 'Mot en avancerad teknisk framtid',
        'our_services': 'Våra Integrerade Tjänster',
        'tech': 'Teknik',
        'tech_desc': 'Nätverksingenjör - Design och installation av dator- och kommunikationsnätverk',
        'maintenance': 'Drift och Underhåll',
        'maintenance_desc': 'Underhåll och drift av tekniska system',
        'construction': 'Bygg',
        'construction_desc': 'Golvläggning - Professionell installation av alla typer av golv',
        'carpet': 'Mattor',
        'carpet_desc': 'Installation av olika typer av mattor',
        'consulting': 'Byggrådgivning',
        'consulting_desc': 'Erfarna byggkonsulter',
        'switch_arabic': 'Arabic',
        'switch_swedish': 'Svenska',
        'switch_english': 'English'
    },
    'en': {
        'title': 'Mugrani & Djerf',
        'home': 'Home',
        'services': 'Services',
        'projects': 'Projects',
        'contact': 'Contact',
        'welcome': 'Welcome to Mugrani & Djerf',
        'tagline': 'A leading company in technology and innovation',
        'slogan': 'Towards an advanced technical future',
        'our_services': 'Our Integrated Services',
        'tech': 'Technology',
        'tech_desc': 'Network Engineering - Design and installation of computer and communication networks',
        'maintenance': 'Operation & Maintenance',
        'maintenance_desc': 'Maintenance and operation of technical systems',
        'construction': 'Construction',
        'construction_desc': 'Flooring Installation - Professional installation of all types of floors',
        'carpet': 'Carpet Installation',
        'carpet_desc': 'Installation of various types of carpets',
        'consulting': 'Building Guidance',
        'consulting_desc': 'Expert building consultations',
        'switch_arabic': 'Arabic',
        'switch_swedish': 'Swedish',
        'switch_english': 'English'
    }
}

@app.route('/')
def home():
    lang = request.args.get('lang', 'ar')
    t = translations.get(lang, translations['ar'])
    
    html_template = '''
    <!DOCTYPE html>
    <html lang="{{ lang }}" dir="{{ 'rtl' if lang == 'ar' else 'ltr' }}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ t.title }}</title>
        <style>
            :root {
                --primary: #667eea;
                --secondary: #764ba2;
                --accent: #f093fb;
                --dark: #2d3748;
                --light: #f7fafc;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Inter', 'Segoe UI', sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
                min-height: 100vh;
                color: var(--dark);
                line-height: 1.6;
                overflow-x: hidden;
            }

            /* تصميم تكنولوجي حديث */
            .tech-bg {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(240, 147, 251, 0.05) 0%, transparent 50%);
                z-index: -1;
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }

            /* Header تكنولوجي */
            header {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                padding: 1rem 0;
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
                border-bottom: 1px solid rgba(255,255,255,0.2);
            }

            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }

            .logo {
                font-size: 2rem;
                font-weight: 800;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-decoration: none;
                position: relative;
            }

            .logo::after {
                content: '';
                position: absolute;
                bottom: -5px;
                left: 0;
                width: 100%;
                height: 3px;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                border-radius: 2px;
            }

            .nav-links {
                display: flex;
                list-style: none;
                gap: 2.5rem;
                align-items: center;
            }

            .nav-links a {
                text-decoration: none;
                color: var(--dark);
                font-weight: 600;
                transition: all 0.3s ease;
                padding: 0.7rem 1.2rem;
                border-radius: 12px;
                position: relative;
                overflow: hidden;
            }

            .nav-links a::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                transition: left 0.3s ease;
                z-index: -1;
                border-radius: 12px;
            }

            .nav-links a:hover {
                color: white;
                transform: translateY(-2px);
            }

            .nav-links a:hover::before {
                left: 0;
            }

            .language-switcher {
                display: flex;
                gap: 0.8rem;
            }

            .lang-btn {
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                color: white;
                border: none;
                padding: 0.7rem 1.2rem;
                border-radius: 25px;
                cursor: pointer;
                text-decoration: none;
                font-size: 0.9rem;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                position: relative;
                overflow: hidden;
            }

            .lang-btn::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, var(--secondary), var(--primary));
                transition: left 0.3s ease;
            }

            .lang-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
            }

            .lang-btn:hover::before {
                left: 0;
            }

            .lang-btn span {
                position: relative;
                z-index: 1;
            }

            /* Hero Section تكنولوجي */
            .hero {
                background: linear-gradient(135deg, 
                    rgba(102, 126, 234, 0.9) 0%, 
                    rgba(118, 75, 162, 0.9) 50%, 
                    rgba(240, 147, 251, 0.7) 100%);
                color: white;
                padding: 180px 0 120px;
                text-align: center;
                margin-top: 80px;
                position: relative;
                overflow: hidden;
            }

            .hero::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 30% 20%, rgba(255,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 70% 80%, rgba(255,255,255,0.1) 0%, transparent 50%);
                animation: float 6s ease-in-out infinite;
            }

            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(-20px) rotate(180deg); }
            }

            .hero h1 {
                font-size: 4rem;
                margin-bottom: 1.5rem;
                font-weight: 800;
                position: relative;
                text-shadow: 0 4px 15px rgba(0,0,0,0.2);
                animation: fadeInUp 1s ease-out;
            }

            .hero p {
                font-size: 1.5rem;
                margin-bottom: 1rem;
                opacity: 0.9;
                position: relative;
                animation: fadeInUp 1s ease-out 0.2s both;
            }

            .hero .slogan {
                font-size: 1.2rem;
                font-style: italic;
                opacity: 0.8;
                animation: fadeInUp 1s ease-out 0.4s both;
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* Sections تكنولوجية */
            .section {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                margin: 4rem 0;
                padding: 5rem 0;
                border-radius: 30px;
                box-shadow: 
                    0 20px 40px rgba(0,0,0,0.1),
                    inset 0 1px 0 rgba(255,255,255,0.2);
                border: 1px solid rgba(255,255,255,0.3);
                position: relative;
                overflow: hidden;
            }

            .section::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
            }

            .section h2 {
                color: var(--dark);
                margin-bottom: 3rem;
                text-align: center;
                font-size: 3rem;
                font-weight: 800;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                position: relative;
            }

            .section h2::after {
                content: '';
                position: absolute;
                bottom: -10px;
                left: 50%;
                transform: translateX(-50%);
                width: 100px;
                height: 4px;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                border-radius: 2px;
            }

            /* Services Grid تكنولوجي */
            .services-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
                gap: 2.5rem;
                margin-top: 3rem;
            }

            .service-card {
                background: linear-gradient(135deg, 
                    rgba(255,255,255,0.9) 0%, 
                    rgba(248, 250, 252, 0.8) 100%);
                padding: 3rem 2.5rem;
                border-radius: 20px;
                text-align: center;
                transition: all 0.4s ease;
                border: 1px solid rgba(255,255,255,0.3);
                position: relative;
                overflow: hidden;
                backdrop-filter: blur(10px);
                box-shadow: 
                    0 10px 30px rgba(0,0,0,0.08),
                    inset 0 1px 0 rgba(255,255,255,0.6);
            }

            .service-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, 
                    rgba(102, 126, 234, 0.1) 0%, 
                    rgba(118, 75, 162, 0.1) 50%, 
                    rgba(240, 147, 251, 0.1) 100%);
                transition: left 0.4s ease;
            }

            .service-card:hover::before {
                left: 0;
            }

            .service-card:hover {
                transform: translateY(-15px) scale(1.02);
                box-shadow: 
                    0 25px 50px rgba(0,0,0,0.15),
                    inset 0 1px 0 rgba(255,255,255,0.6);
            }

            .service-icon {
                font-size: 5rem;
                margin-bottom: 2rem;
                display: block;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
                transition: all 0.3s ease;
            }

            .service-card:hover .service-icon {
                transform: scale(1.1) rotate(5deg);
                filter: drop-shadow(0 6px 12px rgba(0,0,0,0.2));
            }

            .service-card h3 {
                color: var(--dark);
                margin-bottom: 1.5rem;
                font-size: 1.8rem;
                font-weight: 700;
                position: relative;
            }

            .service-card p {
                color: #666;
                line-height: 1.8;
                font-size: 1.1rem;
                position: relative;
            }

            /* باقي الأقسام بنفس النمط التكنولوجي */
            .project-card, .contact-info {
                background: linear-gradient(135deg, 
                    rgba(255,255,255,0.9) 0%, 
                    rgba(248, 250, 252, 0.8) 100%);
                padding: 3rem;
                border-radius: 20px;
                text-align: center;
                margin: 2rem auto;
                max-width: 700px;
                border: 1px solid rgba(255,255,255,0.3);
                backdrop-filter: blur(10px);
                box-shadow: 
                    0 15px 35px rgba(0,0,0,0.1),
                    inset 0 1px 0 rgba(255,255,255,0.6);
                transition: all 0.3s ease;
            }

            .project-card:hover, .contact-info:hover {
                transform: translateY(-5px);
                box-shadow: 
                    0 20px 40px rgba(0,0,0,0.15),
                    inset 0 1px 0 rgba(255,255,255,0.6);
            }

            /* Responsive Design */
            @media (max-width: 768px) {
                .nav-links {
                    display: none;
                }
                
                .hero h1 {
                    font-size: 2.8rem;
                }
                
                .hero {
                    padding: 140px 0 80px;
                }
                
                .section {
                    padding: 3rem 1rem;
                    margin: 2rem 0;
                }
                
                .services-grid {
                    grid-template-columns: 1fr;
                    gap: 2rem;
                }
                
                .service-card {
                    padding: 2.5rem 2rem;
                }
                
                .language-switcher {
                    flex-direction: column;
                    gap: 0.8rem;
                }
            }

            @media (max-width: 480px) {
                .hero h1 {
                    font-size: 2.2rem;
                }
                
                .section h2 {
                    font-size: 2.2rem;
                }
                
                .service-card {
                    padding: 2rem 1.5rem;
                }
            }
        </style>
    </head>
    <body>
        <!-- الخلفية التكنولوجية -->
        <div class="tech-bg"></div>

        <!-- Header -->
        <header>
            <div class="nav-container">
                <a href="#home" class="logo">{{ t.title }}</a>
                <div style="display: flex; align-items: center; gap: 2rem;">
                    <ul class="nav-links">
                        <li><a href="#home">{{ t.home }}</a></li>
                        <li><a href="#services">{{ t.services }}</a></li>
                        <li><a href="#projects">{{ t.projects }}</a></li>
                        <li><a href="#contact">{{ t.contact }}</a></li>
                    </ul>
                    <div class="language-switcher">
                        <a href="?lang=ar" class="lang-btn"><span>{{ t.switch_arabic }}</span></a>
                        <a href="?lang=sv" class="lang-btn"><span>{{ t.switch_swedish }}</span></a>
                        <a href="?lang=en" class="lang-btn"><span>{{ t.switch_english }}</span></a>
                    </div>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <section class="hero" id="home">
            <div class="container">
                <h1>{{ t.welcome }}</h1>
                <p>{{ t.tagline }}</p>
                <p class="slogan">"{{ t.slogan }}"</p>
            </div>
        </section>

        <!-- Services Section -->
        <section class="section" id="services">
            <div class="container">
                <h2>{{ t.our_services }}</h2>
                <div class="services-grid">
                    <!-- التقنية / Technology -->
                    <div class="service-card">
                        <div class="service-icon">🚀</div>
                        <h3>{{ t.tech }}</h3>
                        <p>{{ t.tech_desc }}</p>
                    </div>

                    <!-- التشغيل والصيانة / Operation & Maintenance -->
                    <div class="service-card">
                        <div class="service-icon">⚙️</div>
                        <h3>{{ t.maintenance }}</h3>
                        <p>{{ t.maintenance_desc }}</p>
                    </div>

                    <!-- البناء / Construction -->
                    <div class="service-card">
                        <div class="service-icon">🏗️</div>
                        <h3>{{ t.construction }}</h3>
                        <p>{{ t.construction_desc }}</p>
                    </div>

                    <!-- السجاد / Carpet -->
                    <div class="service-card">
                        <div class="service-icon">🎨</div>
                        <h3>{{ t.carpet }}</h3>
                        <p>{{ t.carpet_desc }}</p>
                    </div>

                    <!-- إرشادات البناء / Consulting -->
                    <div class="service-card">
                        <div class="service-icon">💡</div>
                        <h3>{{ t.consulting }}</h3>
                        <p>{{ t.consulting_desc }}</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section class="section" id="projects">
            <div class="container">
                <h2>{{ t.projects }}</h2>
                <div class="project-card">
                    <h3>🌐 موقع الشركة التكنولوجي</h3>
                    <p>تم تطوير هذا الموقع الاحترافي المتطور باستخدام Python Flask - يدعم ثلاث لغات مختلفة بتصميم تكنولوجي حديث</p>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="section" id="contact">
            <div class="container">
                <h2>{{ t.contact }}</h2>
                <div class="contact-info">
                    <p><strong>📧 Email:</strong> sksomugrani07@gmail.com</p>
                    <p><strong>📧 البريد الإلكتروني:</strong> sksomugrani07@gmail.com</p>
                    <p><strong>📱 Phone / الهاتف:</strong> +46 123 456 789</p>
                </div>
            </div>
        </section>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, t=t, lang=lang)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
