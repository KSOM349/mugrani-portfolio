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
    lang = request.args.get('lang', 'ar')  # اللغة الافتراضية العربية
    
    # الحصول على الترجمة المناسبة
    t = translations.get(lang, translations['ar'])
    
    html_template = '''
    <!DOCTYPE html>
    <html lang="{{ lang }}" dir="{{ 'rtl' if lang == 'ar' else 'ltr' }}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ t.title }}</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                direction: {{ 'rtl' if lang == 'ar' else 'ltr' }};
            }

            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }

            /* Header Styles */
            header {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 1rem 0;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
            }

            .nav-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .logo {
                font-size: 1.5rem;
                font-weight: bold;
                color: #333;
            }

            .nav-links {
                display: flex;
                list-style: none;
                gap: 2rem;
            }

            .nav-links a {
                text-decoration: none;
                color: #333;
                font-weight: 500;
                transition: color 0.3s;
            }

            .nav-links a:hover {
                color: #667eea;
            }

            .language-switcher {
                display: flex;
                gap: 0.5rem;
            }

            .lang-btn {
                background: #667eea;
                color: white;
                border: none;
                padding: 0.4rem 0.8rem;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                font-size: 0.8rem;
                transition: background 0.3s;
            }

            .lang-btn:hover {
                background: #5a6fd8;
            }

            /* Hero Section */
            .hero {
                background: linear-gradient(135deg, rgba(102, 126, 234, 0.9), rgba(118, 75, 162, 0.9));
                color: white;
                padding: 120px 0 80px;
                text-align: center;
                margin-top: 60px;
            }

            .hero h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }

            .hero p {
                font-size: 1.2rem;
                margin-bottom: 1rem;
                opacity: 0.9;
            }

            /* Sections */
            .section {
                background: white;
                margin: 2rem 0;
                padding: 3rem;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }

            .section h2 {
                color: #333;
                margin-bottom: 2rem;
                text-align: center;
                font-size: 2rem;
            }

            /* Services Grid */
            .services-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 2rem;
            }

            .service-card {
                background: #f8f9fa;
                padding: 2rem;
                border-radius: 10px;
                text-align: center;
                transition: transform 0.3s;
                border: 1px solid #e9ecef;
            }

            .service-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }

            .service-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }

            .service-card h3 {
                color: #333;
                margin-bottom: 1rem;
                font-size: 1.3rem;
            }

            .service-card p {
                color: #666;
                line-height: 1.6;
            }

            /* Projects Section */
            .project-card {
                background: #f8f9fa;
                padding: 2rem;
                border-radius: 10px;
                text-align: center;
                margin: 1rem 0;
            }

            /* Contact Section */
            .contact-info {
                text-align: center;
                padding: 2rem;
                background: #f8f9fa;
                border-radius: 10px;
                margin: 1rem 0;
            }

            /* Responsive */
            @media (max-width: 768px) {
                .nav-links {
                    display: none;
                }
                
                .hero h1 {
                    font-size: 2rem;
                }
                
                .section {
                    padding: 2rem 1rem;
                }
                
                .services-grid {
                    grid-template-columns: 1fr;
                }
                
                .language-switcher {
                    flex-direction: column;
                    gap: 0.3rem;
                }
            }
        </style>
    </head>
    <body>
        <!-- Header -->
        <header>
            <div class="nav-container">
                <div class="logo">{{ t.title }}</div>
                <div style="display: flex; align-items: center; gap: 2rem;">
                    <ul class="nav-links">
                        <li><a href="#home">{{ t.home }}</a></li>
                        <li><a href="#services">{{ t.services }}</a></li>
                        <li><a href="#projects">{{ t.projects }}</a></li>
                        <li><a href="#contact">{{ t.contact }}</a></li>
                    </ul>
                    <div class="language-switcher">
                        <a href="?lang=ar" class="lang-btn">{{ t.switch_arabic }}</a>
                        <a href="?lang=sv" class="lang-btn">{{ t.switch_swedish }}</a>
                        <a href="?lang=en" class="lang-btn">{{ t.switch_english }}</a>
                    </div>
                </div>
            </div>
        </header>

        <!-- Hero Section -->
        <section class="hero" id="home">
            <div class="container">
                <h1>{{ t.welcome }}</h1>
                <p>{{ t.tagline }}</p>
                <p>"{{ t.slogan }}"</p>
            </div>
        </section>

        <!-- Services Section -->
        <section class="section" id="services">
            <div class="container">
                <h2>{{ t.our_services }}</h2>
                <div class="services-grid">
                    <!-- التقنية / Technology -->
                    <div class="service-card">
                        <div class="service-icon">🖥️</div>
                        <h3>{{ t.tech }}</h3>
                        <p>{{ t.tech_desc }}</p>
                    </div>

                    <!-- التشغيل والصيانة / Operation & Maintenance -->
                    <div class="service-card">
                        <div class="service-icon">🔧</div>
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
                        <div class="service-icon">📋</div>
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
                    <h3>Company Website</h3>
                    <p>This professional website developed with Python Flask - supporting multiple languages</p>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="section" id="contact">
            <div class="container">
                <h2>{{ t.contact }}</h2>
                <div class="contact-info">
                    <p><strong>Email:</strong> sksomugrani07@gmail.com</p>
                    <p><strong>البريد الإلكتروني:</strong> sksomugrani07@gmail.com</p>
                </div>
            </div>
        </section>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, t=t, lang=lang)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
