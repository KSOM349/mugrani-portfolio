from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'fixed_projects_key'

@app.route('/')
def home():
    lang = session.get('lang', 'arabic')
    return render_fixed_home(lang)

@app.route('/switch/<language>')
def switch_language(language):
    if language in ['arabic', 'svenska', 'english']:
        session['lang'] = language
    return home()

def render_fixed_home(lang):
    # محتوى متكامل للغات الثلاث - مع المشاريع المترجمة
    content = {
        'arabic': {
            'title': '🚀 مغراني و جيرف',
            'welcome': 'مرحباً بكم في شركتنا!',
            'select_lang': 'اختر لغة من الأعلى',
            'company_desc': 'شركة رائدة في مجال التقنية والابتكار',
            'tech_slogan': 'نحو مستقبل تقني متطور',
            'services_title': 'خدماتنا المتكاملة',
            'why_choose_us': 'لماذا تختارنا',
            'projects_title': 'أحدث مشاريعنا',
            'reviews_title': 'آراء عملائنا',
            'stats_title': 'أرقامنا تتحدث',
            'contact_info': 'معلومات الاتصال',
            'nav_home': 'الرئيسية',
            'nav_about': 'من نحن',
            'nav_services': 'خدماتنا',
            'nav_contact': 'اتصل بنا',
            'advantages': [
                'حلول متكاملة من التقنية إلى البناء',
                'فريق متعدد التخصصات',
                'خبرة طويلة في المجال',
                'خدمة متعددة اللغات'
            ],
            'projects': [
                {'icon': '🏢', 'title': 'شبكة شركة تقنية', 'desc': 'تركيب شبكة كاملة لشركة تقنية في ستوكهولم'},
                {'icon': '🏠', 'title': 'تجهيز فيلا فاخرة', 'desc': 'تركيب أرضيات وسجاد لفيلا جديدة في أوبسالا'},
                {'icon': '🏭', 'title': 'صيانة نظام مصنع', 'desc': 'صيانة الأنظمة التقنية لمصنع محلي'}
            ],
            'reviews': [
                {'name': 'أحمد الخالد', 'service': 'تركيب شبكات', 'comment': 'فريق محترف وأنهى العمل قبل الوقت المحدد', 'rating': '★★★★★'},
                {'name': 'ماريا اندرسون', 'service': 'تركيب أرضيات', 'comment': 'دقة في العمل وأناقة في التنفيذ', 'rating': '★★★★★'},
                {'name': 'جون بيرسون', 'service': 'صيانة أنظمة', 'comment': 'استجابة سريعة وحلول فعالة', 'rating': '★★★★☆'}
            ],
            'stats': [
                {'number': '50+', 'label': 'مشروع مكتمل'},
                {'number': '5+', 'label': 'سنوات خبرة'},
                {'number': '98%', 'label': 'عملاء راضون'},
                {'number': '24h', 'label': 'استجابة سريعة'}
            ]
        },
        'svenska': {
            'title': '🚀 Mugrani & Djerf Ab',
            'welcome': 'Välkommen till vårt företag!',
            'select_lang': 'Välj ett språk ovan',
            'company_desc': 'Ett ledande företag inom teknik och innovation',
            'tech_slogan': 'Mot en avancerad teknisk framtid',
            'services_title': 'Våra Integrerade Tjänster',
            'why_choose_us': 'Varför Välja Oss',
            'projects_title': 'Våra Senaste Projekt',
            'reviews_title': 'Kundomdömen',
            'stats_title': 'Våra Siffror Talar',
            'contact_info': 'Kontaktinformation',
            'nav_home': 'Hem',
            'nav_about': 'Om oss',
            'nav_services': 'Tjänster',
            'nav_contact': 'Kontakt',
            'advantages': [
                'Integrerade lösningar från teknik till byggnad',
                'Mångsidigt team med olika kompetenser',
                'Lång erfarenhet i branschen',
                'Flerspråkig service'
            ],
            'projects': [
                {'icon': '🏢', 'title': 'Tekniföretags Nätverk', 'desc': 'Fullständig nätverksinstallation för ett teknikföretag i Stockholm'},
                {'icon': '🏠', 'title': 'Lyxvilla Utrustning', 'desc': 'Golv- och mattläggning för en ny lyxvilla i Uppsala'},
                {'icon': '🏭', 'title': 'Fabrikssystem Underhåll', 'desc': 'Underhåll av tekniska system för en lokal fabrik'}
            ],
            'reviews': [
                {'name': 'Ahmed Al-Khalid', 'service': 'Nätverksinstallation', 'comment': 'Professionellt team som slutförde arbetet före deadline', 'rating': '★★★★★'},
                {'name': 'Maria Andersson', 'service': 'Golvläggning', 'comment': 'Noggrannhet i arbetet och elegans i utförandet', 'rating': '★★★★★'},
                {'name': 'John Persson', 'service': 'Systemunderhåll', 'comment': 'Snabbt svar och effektiva lösningar', 'rating': '★★★★☆'}
            ],
            'stats': [
                {'number': '50+', 'label': 'Avslutade Projekt'},
                {'number': '5+', 'label': 'Års Erfarenhet'},
                {'number': '98%', 'label': 'Nöjda Kunder'},
                {'number': '24h', 'label': 'Snabbt Svar'}
            ]
        },
        'english': {
            'title': '🚀 Mugrani & Djerf Ltd',
            'welcome': 'Welcome to our company!',
            'select_lang': 'Select a language above',
            'company_desc': 'A leading company in technology and innovation',
            'tech_slogan': 'Towards an advanced technological future',
            'services_title': 'Our Integrated Services',
            'why_choose_us': 'Why Choose Us',
            'projects_title': 'Our Latest Projects',
            'reviews_title': 'Customer Reviews',
            'stats_title': 'Our Numbers Speak',
            'contact_info': 'Contact Information',
            'nav_home': 'Home',
            'nav_about': 'About',
            'nav_services': 'Services',
            'nav_contact': 'Contact',
            'advantages': [
                'Integrated solutions from technology to construction',
                'Multidisciplinary team with diverse expertise',
                'Long experience in the field',
                'Multilingual service'
            ],
            'projects': [
                {'icon': '🏢', 'title': 'Tech Company Network', 'desc': 'Complete network installation for a tech company in Stockholm'},
                {'icon': '🏠', 'title': 'Luxury Villa Setup', 'desc': 'Floor and carpet installation for a new luxury villa in Uppsala'},
                {'icon': '🏭', 'title': 'Factory System Maintenance', 'desc': 'Maintenance of technical systems for a local factory'}
            ],
            'reviews': [
                {'name': 'Ahmed Al-Khalid', 'service': 'Network Installation', 'comment': 'Professional team that completed work ahead of schedule', 'rating': '★★★★★'},
                {'name': 'Maria Andersson', 'service': 'Floor Installation', 'comment': 'Precision in work and elegance in execution', 'rating': '★★★★★'},
                {'name': 'John Persson', 'service': 'System Maintenance', 'comment': 'Quick response and effective solutions', 'rating': '★★★★☆'}
            ],
            'stats': [
                {'number': '50+', 'label': 'Completed Projects'},
                {'number': '5+', 'label': 'Years Experience'},
                {'number': '98%', 'label': 'Satisfied Customers'},
                {'number': '24h', 'label': 'Quick Response'}
            ]
        }
    }
    
    # استخدام آمن مع قيمة افتراضية
    def get_text(key):
        return content.get(lang, content['arabic']).get(key, key)
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{get_text('title')}</title>
        <style>
            /* التصميم التكنولوجي الكامل */
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
                min-height: 100vh;
                color: #ffffff;
                overflow-x: hidden;
                position: relative;
            }}

            /* الشبكة التكنولوجية */
            .tech-grid {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px),
                    linear-gradient(0deg, rgba(255,255,255,0.03) 1px, transparent 1px);
                background-size: 50px 50px;
                animation: gridMove 20s linear infinite;
                z-index: -2;
            }}

            @keyframes gridMove {{
                0% {{ transform: translate(0, 0); }}
                100% {{ transform: translate(50px, 50px); }}
            }}

            /* الدوائر المتحركة */
            .tech-circles {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                overflow: hidden;
            }}

            .circle {{
                position: absolute;
                border: 2px solid rgba(0, 150, 255, 0.3);
                border-radius: 50%;
                animation: pulse 4s ease-in-out infinite;
            }}

            .circle:nth-child(1) {{
                width: 300px;
                height: 300px;
                top: 10%;
                left: 10%;
                animation-delay: 0s;
            }}

            .circle:nth-child(2) {{
                width: 200px;
                height: 200px;
                top: 60%;
                right: 10%;
                animation-delay: 1s;
                border-color: rgba(0, 255, 150, 0.3);
            }}

            .circle:nth-child(3) {{
                width: 400px;
                height: 400px;
                bottom: 10%;
                left: 20%;
                animation-delay: 2s;
                border-color: rgba(255, 100, 0, 0.3);
            }}

            .circle:nth-child(4) {{
                width: 150px;
                height: 150px;
                top: 20%;
                right: 20%;
                animation-delay: 3s;
                border-color: rgba(150, 0, 255, 0.3);
            }}

            @keyframes pulse {{
                0%, 100% {{ 
                    transform: scale(1);
                    opacity: 0.3;
                }}
                50% {{ 
                    transform: scale(1.1);
                    opacity: 0.6;
                }}
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}

            .top-bar {{
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(15px);
                padding: 20px 0;
                border-radius: 20px;
                margin-bottom: 40px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }}

            .logo {{
                font-size: 2.8em;
                font-weight: bold;
                text-align: center;
                margin-bottom: 15px;
                background: linear-gradient(45deg, #00b4db, #0083b0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}

            .language-switcher {{
                display: flex;
                justify-content: center;
                gap: 25px;
                flex-wrap: wrap;
            }}

            .lang-btn {{
                background: linear-gradient(45deg, rgba(0, 180, 219, 0.2), rgba(0, 131, 176, 0.2));
                border: 1px solid rgba(0, 180, 219, 0.3);
                color: #00b4db;
                padding: 12px 30px;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s ease;
            }}

            .lang-btn:hover {{
                background: linear-gradient(45deg, rgba(0, 180, 219, 0.3), rgba(0, 131, 176, 0.3));
                transform: translateY(-3px);
                color: #ffffff;
            }}

            .main-content {{
                text-align: center;
                padding: 80px 40px;
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(20px);
                border-radius: 25px;
                margin: 50px 0;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .welcome-title {{
                font-size: 3.5em;
                margin-bottom: 20px;
                background: linear-gradient(45deg, #00b4db, #00db8b);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}

            .section {{
                margin: 80px 0;
                text-align: center;
            }}

            .section-title {{
                font-size: 2.5em;
                margin-bottom: 50px;
                background: linear-gradient(45deg, #00b4db, #00db8b);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}

            .service-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin: 40px 0;
            }}

            .service-category {{
                background: rgba(255, 255, 255, 0.05);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .service-item {{
                background: rgba(255, 255, 255, 0.03);
                padding: 20px;
                margin: 15px 0;
                border-radius: 10px;
                border-left: 4px solid #00b4db;
                text-align: right;
            }}

            .service-icon {{
                font-size: 2em;
                margin-bottom: 10px;
            }}

            .advantages-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }}

            .advantage-card {{
                background: rgba(255, 255, 255, 0.05);
                padding: 25px;
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .projects-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin: 40px 0;
            }}

            .project-card {{
                background: rgba(255, 255, 255, 0.05);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: transform 0.3s ease;
            }}

            .project-card:hover {{
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.08);
            }}

            .project-icon {{
                font-size: 3em;
                margin-bottom: 15px;
            }}

            .reviews-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
                margin: 40px 0;
            }}

            .review-card {{
                background: rgba(255, 255, 255, 0.05);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .review-rating {{
                color: #ffd700;
                font-size: 1.2em;
                margin: 10px 0;
            }}

            .review-service {{
                color: #00b4db;
                font-style: italic;
            }}

            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 30px;
                margin: 40px 0;
            }}

            .stat-card {{
                background: rgba(255, 255, 255, 0.05);
                padding: 30px;
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .stat-number {{
                font-size: 3em;
                font-weight: bold;
                background: linear-gradient(45deg, #00b4db, #00db8b);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }}

            .contact-info {{
                font-size: 1.2em;
                line-height: 2;
            }}

            .nav-bar {{
                display: flex;
                justify-content: center;
                gap: 35px;
                margin-top: 50px;
                flex-wrap: wrap;
            }}

            .nav-item {{
                background: linear-gradient(45deg, rgba(0, 180, 219, 0.15), rgba(0, 219, 139, 0.15));
                padding: 18px 35px;
                border-radius: 15px;
                text-decoration: none;
                color: #00b4db;
                font-weight: bold;
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 180, 219, 0.2);
            }}

            .nav-item:hover {{
                background: linear-gradient(45deg, rgba(0, 180, 219, 0.3), rgba(0, 219, 139, 0.3));
                transform: translateY(-5px);
                color: #ffffff;
            }}

            @media (max-width: 768px) {{
                .welcome-title {{ font-size: 2.5em; }}
                .language-switcher {{ gap: 15px; }}
                .nav-bar {{ gap: 20px; }}
                .main-content {{ padding: 40px 20px; }}
            }}
        </style>
    </head>
    <body>
        <!-- الخلفية التكنولوجية -->
        <div class="tech-grid"></div>
        <div class="tech-circles">
            <div class="circle"></div>
            <div class="circle"></div>
            <div class="circle"></div>
            <div class="circle"></div>
        </div>

        <div class="container">
            <div class="top-bar">
                <div class="logo">{get_text('title')}</div>
                <div class="language-switcher">
                    <a href="/switch/arabic" class="lang-btn">العربية 🇸🇦</a>
                    <a href="/switch/svenska" class="lang-btn">Svenska 🇸🇪</a>
                    <a href="/switch/english" class="lang-btn">English 🇺🇸</a>
                </div>
            </div>

            <div class="main-content">
                <h1 class="welcome-title">{get_text('welcome')}</h1>
                <p style="font-size: 1.3em; color: #cccccc; margin-bottom: 20px;">{get_text('select_lang')}</p>
                <p style="font-size: 1.2em; color: #aaaaaa; max-width: 700px; margin: 0 auto 30px;">{get_text('company_desc')}</p>
                <p style="font-size: 1.1em; color: #00b4db; font-style: italic; margin-bottom: 50px;">"{get_text('tech_slogan')}"</p>

                <!-- خدماتنا -->
                <div class="section">
                    <h2 class="section-title">{get_text('services_title')}</h2>
                    <div class="service-grid">
                        <div class="service-category">
                            <h3 style="color: #00b4db; margin-bottom: 20px;">🖥️ {get_text('nav_services') if lang == 'arabic' else 'Technology' if lang == 'english' else 'Teknik'}</h3>
                            <div class="service-item">
                                <div class="service-icon">🖥️</div>
                                <h4>هندسة الشبكات</h4>
                                <p>تصميم وتركيب شبكات الحاسب والاتصالات</p>
                            </div>
                            <div class="service-item">
                                <div class="service-icon">🔧</div>
                                <h4>تشغيل وصيانة</h4>
                                <p>صيانة وتشغيل الأنظمة التقنية</p>
                            </div>
                        </div>
                        
                        <div class="service-category">
                            <h3 style="color: #00db8b; margin-bottom: 20px;">🏗️ {get_text('nav_about') if lang == 'arabic' else 'Construction' if lang == 'english' else 'Bygg'}</h3>
                            <div class="service-item">
                                <div class="service-icon">🏠</div>
                                <h4>تركيب الأرضيات</h4>
                                <p>تركيب جميع أنواع الأرضيات باحترافية</p>
                            </div>
                            <div class="service-item">
                                <div class="service-icon">🎨</div>
                                <h4>تركيب السجاد</h4>
                                <p>تركيب السجاد بأنواعه المختلفة</p>
                            </div>
                            <div class="service-item">
                                <div class="service-icon">🏗️</div>
                                <h4>إرشادات البناء</h4>
                                <p>استشارات بناء من ذوي الخبرة</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- لماذا تختارنا -->
                <div class="section">
                    <h2 class="section-title">{get_text('why_choose_us')}</h2>
                    <div class="advantages-grid">
                        {' '.join([f'''
                        <div class="advantage-card">
                            <h4>✅ {advantage}</h4>
                        </div>
                        ''' for advantage in content[lang]['advantages']])}
                    </div>
                </div>

                <!-- أحدث المشاريع - الآن مترجمة -->
                <div class="section">
                    <h2 class="section-title">{get_text('projects_title')}</h2>
                    <div class="projects-grid">
                        {' '.join([f'''
                        <div class="project-card">
                            <div class="project-icon">{project["icon"]}</div>
                            <h3>{project["title"]}</h3>
                            <p>{project["desc"]}</p>
                        </div>
                        ''' for project in content[lang]['projects']])}
                    </div>
                </div>

                <!-- آراء العملاء -->
                <div class="section">
                    <h2 class="section-title">{get_text('reviews_title')}</h2>
                    <div class="reviews-grid">
                        {' '.join([f'''
                        <div class="review-card">
                            <div class="review-rating">{review["rating"]}</div>
                            <p>"{review["comment"]}"</p>
                            <div class="review-service">- {review["service"]}</div>
                            <strong>{review["name"]}</strong>
                        </div>
                        ''' for review in content[lang]['reviews']])}
                    </div>
                </div>

                <!-- الإحصائيات -->
                <div class="section">
                    <h2 class="section-title">{get_text('stats_title')}</h2>
                    <div class="stats-grid">
                        {' '.join([f'''
                        <div class="stat-card">
                            <div class="stat-number">{stat["number"]}</div>
                            <h3>{stat["label"]}</h3>
                        </div>
                        ''' for stat in content[lang]['stats']])}
                    </div>
                </div>

                <!-- معلومات الاتصال -->
                <div class="section">
                    <h2 class="section-title">{get_text('contact_info')}</h2>
                    <div class="contact-info">
                        <p>📧 info@mugrani-djerf.com</p>
                        <p>📞 +46 123 456 789</p>
                        <p>📍 { 'ستوكهولم، السويد' if lang == 'arabic' else 'Stockholm, Sverige' if lang == 'svenska' else 'Stockholm, Sweden' }</p>
                    </div>
                </div>

                <!-- شريط التنقل -->
                <div class="nav-bar">
                    <a href="#" class="nav-item">{get_text('nav_home')}</a>
                    <a href="#" class="nav-item">{get_text('nav_about')}</a>
                    <a href="#" class="nav-item">{get_text('nav_services')}</a>
                    <a href="#" class="nav-item">{get_text('nav_contact')}</a>
                </div>
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                console.log('🚀 الموقع المصحح يعمل بنجاح! المشاريع الآن تترجم!');
            }});
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("🎯 الموقع المصحح يعمل على: http://localhost:5000")
    print("✅ قسم المشاريع الآن يترجم مع جميع اللغات!")
    app.run(host='0.0.0.0', port=5000, debug=True)
