from __future__ import annotations

import datetime as dt
import html
import json
import re
import unicodedata
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://oleksii-tumanov.github.io/publications/"
RESEARCHGATE_PROFILE_URL = "https://www.researchgate.net/profile/Oleksii-Tumanov-2"
ORCID_PROFILE_URL = "https://orcid.org/0000-0003-0674-0037"

CYRILLIC_MAP = str.maketrans(
    {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "H",
        "Ґ": "G",
        "Д": "D",
        "Е": "E",
        "Є": "Ie",
        "Ж": "Zh",
        "З": "Z",
        "И": "Y",
        "І": "I",
        "Ї": "Yi",
        "Й": "Y",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ь": "",
        "Ю": "Yu",
        "Я": "Ya",
        "Ъ": "",
        "Ы": "Y",
        "Э": "E",
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "yi",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "yu",
        "я": "ya",
        "ъ": "",
        "ы": "y",
        "э": "e",
    }
)

PUBLICATIONS = [
    {
        "title": "Large Language Models: A New Paradigm for Data Analysis",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2025,
        "journal_title": "Business Inform",
        "venue_display": "Business Inform",
        "volume": "9",
        "issue": "572",
        "first_page": "106",
        "last_page": "113",
        "doi": "10.32983/2222-4459-2025-9-106-113",
        "issn": "2222-4459",
        "lang": "en",
        "citations": 0,
        "abstract": (
            "The article examines how large language models are changing data analysis across "
            "domains such as social media analytics, healthcare, and software development. It "
            "compares LLM-based approaches with traditional statistical methods across data type, "
            "interpretability, purpose, data requirements, and reproducibility, and argues that the "
            "strongest future direction is hybrid methodology that combines LLM preprocessing with "
            "classical statistical analysis for greater transparency, reliability, and accuracy."
        ),
        "links": [
            ("DOI record", "https://doi.org/10.32983/2222-4459-2025-9-106-113"),
            ("Publisher PDF", "https://www.business-inform.net/export_pdf/business-inform-2025-9_0-pages-106_113.pdf"),
            ("Publisher article page", "https://www.business-inform.net/article/?abstract=2025_9_0_106_113&lang=en&year=2025"),
            ("ResearchGate entry", "https://www.researchgate.net/publication/398006520_Large_Language_Models_A_New_Paradigm_for_Data_Analysis"),
        ],
        "featured": True,
    },
    {
        "title": "THE EVOLUTION OF DATA ANALYSIS TOOLS: FROM SPREADSHEETS TO ARTIFICIAL INTELLIGENCE AGENTS",
        "authors": ["Oleksii Tumanov"],
        "citation_authors": ["Tumanov, Oleksii"],
        "year": 2025,
        "journal_title": "Modern engineering and innovative technologies",
        "venue_display": "Modern engineering and innovative technologies",
        "doi": "10.30890/2567-5273.2025-42-03-055",
        "issn": "2567-5273",
        "issue": "42-03",
        "first_page": "110",
        "last_page": "120",
        "lang": "en",
        "abstract": (
            "This review article traces the evolution of data analysis tools from spreadsheets and "
            "corporate BI platforms to cloud-native data stacks and agentic systems built on large "
            "language models. It examines the methodological shift from syntax-centered work to "
            "semantic layers, reproducibility, orchestration, and evaluation-by-design, and argues "
            "that the most promising direction is an integrated analytical environment where "
            "traditional statistical tools, modern data platforms, and AI agents complement rather "
            "than replace one another."
        ),
        "links": [
            ("DOI record", "https://doi.org/10.30890/2567-5273.2025-42-03-055"),
            ("Publisher PDF", "https://www.moderntechno.de/index.php/meit/article/download/meit42-03-055/9900"),
            ("Publisher article page", "https://www.moderntechno.de/index.php/meit/article/view/meit42-03-055"),
        ],
        "featured": True,
    },
    {
        "title": "MULTIMODAL AUDIO ANALYSIS IN SOCIAL MEDIA: AN AI-DRIVEN APPROACH TO EMOTIONAL INSIGHT",
        "authors": ["Oleksii Tumanov"],
        "citation_authors": ["Tumanov, Oleksii"],
        "year": 2025,
        "journal_title": "Sworld-Us Conference proceedings",
        "venue_display": "Sworld-Us Conference proceedings",
        "doi": "10.30888/2709-2267.2025-33-00-018",
        "issn": "2709-2267",
        "issue": "usc33-00",
        "first_page": "25",
        "last_page": "31",
        "lang": "en",
        "citations": 0,
        "links": [
            ("DOI record", "https://doi.org/10.30888/2709-2267.2025-33-00-018"),
            ("Publisher PDF", "https://www.proconference.org/index.php/usc/article/download/usc33-00-018/3230"),
            ("Publisher article page", "https://www.proconference.org/index.php/usc/article/view/usc33-00-018"),
        ],
        "featured": True,
    },
    {
        "title": "Multimodal sentiment analysis in social media: a statistical framework for uncovering visual-textual divergence",
        "authors": ["Oleksii Tumanov"],
        "citation_authors": ["Tumanov, Oleksii"],
        "alternate_titles": [
            "Мультимодальний аналіз настроїв у соціальних мережах: статистична основа для виявлення візуально-текстової дивергенції",
        ],
        "year": 2025,
        "conference_title": (
            "Proceedings of the International Scientific Conference "
            "“Integration of Science and Innovation for Sustainable Development”"
        ),
        "venue_display": (
            "Proceedings of the International Scientific Conference "
            "“Integration of Science and Innovation for Sustainable Development”"
        ),
        "first_page": "21",
        "last_page": "23",
        "lang": "en",
        "abstract": (
            "This conference paper proposes a statistical framework for multimodal sentiment "
            "analysis in social media, with a focus on detecting divergence between visual and "
            "textual signals in the same post. It positions visual-textual divergence as an "
            "analytically useful phenomenon for understanding ambiguity, irony, and inconsistent "
            "affective cues across social media content."
        ),
        "links": [
            ("Proceedings DOI", "https://doi.org/10.64076/iedc250821"),
            ("Proceedings PDF", "https://researcheurope.org/wp-content/uploads/2025/09/re-21.08.2025.pdf"),
        ],
        "featured": True,
    },
    {
        "title": "THE UNSEEN DATA: A STATISTICAL AND ENGINEERING PERSPECTIVE ON BIASES IN LARGE LANGUAGE MODELS",
        "authors": ["Oleksii Tumanov"],
        "citation_authors": ["Tumanov, Oleksii"],
        "year": 2025,
        "journal_title": "SWorldJournal",
        "venue_display": "SWorldJournal",
        "volume": "1",
        "issue": "33-01",
        "first_page": "179",
        "last_page": "187",
        "doi": "10.30888/2663-5712.2025-33-01-078",
        "issn": "2663-5712",
        "lang": "en",
        "abstract": (
            "This paper frames bias in large language models as a statistical and engineering "
            "problem rooted in non-representative training corpora, demographic "
            "underrepresentation, and distorted parameter estimation. It distinguishes data-driven "
            "bias from model-based bias and argues that mitigation requires both better sampling "
            "discipline and engineering controls throughout model development and evaluation."
        ),
        "links": [
            ("DOI record", "https://doi.org/10.30888/2663-5712.2025-33-01-078"),
            ("Publisher PDF", "https://www.sworldjournal.com/index.php/swj/article/download/swj33-01-078/6044/2631"),
            ("Publisher article page", "https://www.sworldjournal.com/index.php/swj/article/view/swj33-01-078"),
        ],
        "featured": True,
    },
    {
        "title": "МУЛЬТИМОДАЛЬНИЙ АНАЛІЗ ДАНИХ ІЗ СОЦІАЛЬНИХ МЕРЕЖ: ІНТЕГРАЦІЯ АУДІО ТА ТЕКСТУ ЗА ДОПОМОГОЮ ШІ",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2025,
        "conference_title": "Global trends in science and education. Abstracts of the 9th International scientific and practical conference",
        "venue_display": "Global trends in science and education. Abstracts of the 9th International scientific and practical conference",
        "first_page": "220",
        "last_page": "226",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2025/09/GLOBAL-TRENDS-IN-SCIENCE-AND-EDUCATION-22-24.09.2025.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/ix-mizhnarodna-naukovo-praktichna-konferentsiya-global-trends-in-science-and-education-22-24-09-2025-kiyiv-ukrayina-arhiv/"),
        ],
    },
    {
        "title": "РОЗРОБКА СИСТЕМИ СТАТИСТИЧНИХ ПОКАЗНИКІВ ДЛЯ МОНІТОРИНГУ ЕМОЦІЙНОГО СТАНУ У СОЦІАЛЬНИХ МЕДІА",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2025,
        "conference_title": "Socio-economic development in the context of today’s challenges: proceedings of the III International scientific and practical conference",
        "venue_display": "Socio-economic development in the context of today’s challenges: proceedings of the III International scientific and practical conference",
        "first_page": "114",
        "last_page": "118",
        "lang": "uk",
        "links": [
            ("Proceedings DOI", "https://doi.org/10.64076/eecsr250816"),
            ("Proceedings PDF", "https://researcheurope.org/wp-content/uploads/2025/08/re-16.08.2025.pdf"),
        ],
    },
    {
        "title": "Statistical methods for analyzing social media data.",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "journal_title": "Business Inform",
        "venue_display": "Business Inform",
        "volume": "2",
        "issue": "505",
        "doi": "10.32983/2222-4459-2020-2-266-272",
        "issn": "2222-4459",
        "first_page": "266",
        "last_page": "272",
        "lang": "en",
        "citations": 12,
        "links": [
            ("DOI record", "https://doi.org/10.32983/2222-4459-2020-2-266-272"),
            ("Publisher PDF", "https://www.business-inform.net/export_pdf/business-inform-2020-2_0-pages-266_272.pdf"),
            ("Publisher article page", "https://www.business-inform.net/article/?year=2020&abstract=2020_2_0_266_272&lang=en"),
        ],
        "featured": True,
    },
    {
        "title": "Статистичне прогнозування кількості інтернет-користувачів в Україні",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "conference_title": "Modern science: problems and innovations. Abstracts of the 1st International scientific and practical conference.",
        "venue_display": "Modern science: problems and innovations. Abstracts of the 1st International scientific and practical conference.",
        "volume": "1",
        "first_page": "697",
        "last_page": "703",
        "lang": "uk",
        "citations": 2,
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/04/MODERN-SCIENCE-PROBLEMS-AND-INNOVATIONS-5-7.04.20.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/i-mezhdunarodnaya-nauchno-prakticheskaya-konferentsiya-modern-science-problems-and-innovations-5-7-aprelya-2020-goda-stokgolm-shvetsiya-arhiv/"),
            ("WorldCat ISBN record", "https://www.worldcat.org/isbn/9789187224072"),
        ],
    },
    {
        "title": "Statistical evaluation of social media development",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "alternate_titles": ["Статистичне оцінювання розвитку соціальних медіа в Україні"],
        "year": 2020,
        "venue_display": "Author abstract for the PhD dissertation “Statistical evaluation of social media development in Ukraine”",
        "lang": "en",
        "citations": 2,
        "abstract": (
            "This dissertation abstract outlines a statistical framework for evaluating the "
            "development of social media in Ukraine. The public record highlights contributions in "
            "indicator design, information support built from multiple data sources, regional "
            "clustering methods, and forecasting approaches for internet and mobile-device use."
        ),
        "links": [
            ("Author abstract PDF", "https://nasoa.edu.ua/wp-content/uploads/zah/tumanov_avt.pdf"),
            ("Dissertation repository record", "https://uacademic.info/ua/document/0421U100990"),
        ],
    },
    {
        "title": "ФОРМУВАННЯ СИСТЕМИ СТАТИСТИЧНИХ ПОКАЗНИКІВ ДЛЯ ДОСЛІДЖЕННЯ СОЦІАЛЬНИХ МЕДІА В УКРАЇНІ",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "journal_title": "Investytsiyi: praktyka ta dosvid",
        "venue_display": "Investytsiyi: praktyka ta dosvid",
        "doi": "10.32702/2306-6814.2020.5-6.66",
        "issn": "2306-6814",
        "issue": "5-6",
        "first_page": "66",
        "last_page": "71",
        "lang": "uk",
        "links": [
            ("DOI record", "https://doi.org/10.32702/2306-6814.2020.5-6.66"),
            ("Publisher PDF", "http://www.investplan.com.ua/pdf/5-6_2020/12.pdf"),
            ("Publisher article page", "http://www.investplan.com.ua/?op=1&z=7071&i=9"),
        ],
    },
    {
        "title": "ОГЛЯД СТАТИСТИЧНИХ ПОКАЗНИКІВ В ДОСЛІДЖЕННЯХ СОЦІАЛЬНИХ МЕДІА",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "conference_title": "Eurasian scientific congress. Abstracts of the 6th International scientific and practical conference",
        "venue_display": "Eurasian scientific congress. Abstracts of the 6th International scientific and practical conference",
        "first_page": "435",
        "last_page": "437",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/03/EURASIAN-SCIENTIFIC-CONGRESS_22-24.03.20.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/vi-mezhdunarodnaya-nauchno-prakticheskaya-konferencziya-eurasian-scientific-congress-22-24-marta-2020-goda-barselona-ispaniya-arhiv/"),
        ],
    },
    {
        "title": "Developing Social Media in Ukraine: Statistical Forecasting",
        "authors": ["O. Tumanov"],
        "citation_authors": ["Tumanov, O."],
        "year": 2020,
        "journal_title": "Scientific Bulletin of the National Academy of Statistics, Accounting and Audit",
        "venue_display": "Scientific Bulletin of the National Academy of Statistics, Accounting and Audit",
        "doi": "10.31767/nasoa.1-2.2020.03",
        "issn": "2521-1323",
        "issue": "1-2",
        "first_page": "30",
        "last_page": "39",
        "lang": "en",
        "links": [
            ("DOI record", "https://doi.org/10.31767/nasoa.1-2.2020.03"),
            ("Publisher PDF", "https://nasoa-journal.com.ua/index.php/journal/article/download/203/198"),
            ("Publisher article page", "https://nasoa-journal.com.ua/index.php/journal/article/view/203"),
        ],
    },
    {
        "title": "СОЦІАЛЬНІ МЕДІА ЯК ІНСТРУМЕНТ ДОСЛІДЖЕННЯ",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "conference_title": "Dynamics of the development of world science. Abstracts of the 6th International scientific and practical conference",
        "venue_display": "Dynamics of the development of world science. Abstracts of the 6th International scientific and practical conference",
        "first_page": "1142",
        "last_page": "1144",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/02/dynamics-of-the-development-of-world-science_19-21.02.2020.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/vi-mezhdunarodnaya-nauchno-prakticheskaya-k/"),
        ],
    },
    {
        "title": "До питання становлення поняття «соціальні медіа»",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "conference_title": "Science, society, education: topical issues and development prospects. Abstracts of the II International scientific and practical conference",
        "venue_display": "Science, society, education: topical issues and development prospects. Abstracts of the II International scientific and practical conference",
        "first_page": "680",
        "last_page": "681",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/01/science-society-education_topical-issues-and-development-prospects_20-21.01.2020.pdf"),
        ],
    },
    {
        "title": "ПРОБЛЕМИ СТАТИСТИЧНОГО ОЦІНЮВАННЯ СОЦІАЛЬНИХ МЕДІА",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "conference_title": "Topical issues of the development of modern science. Abstracts of the 5th International scientific and practical conference",
        "venue_display": "Topical issues of the development of modern science. Abstracts of the 5th International scientific and practical conference",
        "first_page": "954",
        "last_page": "956",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/01/topical-issues-of-the-development-of-modern-science_15-17.01.2020.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/v-mezhdunarodnaya-nauchno-prakticheskaya-konferencziya-topical-issues-of-the-development-of-modern-science-15-17-yanvarya-2020-goda-sofiya-bolgariya-arhiv/"),
        ],
    },
    {
        "title": "АНАЛІЗ ВПЛИВУ СОЦІАЛЬНИХ МЕДІА НА РОЗВИТОК БІЗНЕС-ОРГАНІЗАЦІЙ",
        "authors": ["Oleksii O. Tumanov", "O. V. Tumanova"],
        "citation_authors": ["Tumanov, Oleksii O.", "Tumanova, O. V."],
        "year": 2020,
        "conference_title": "Scientific achievements of modern society. Abstracts of the 5th International scientific and practical conference.",
        "venue_display": "Scientific achievements of modern society. Abstracts of the 5th International scientific and practical conference.",
        "first_page": "997",
        "last_page": "1000",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/01/scientific-achievements-of-modern-society-v.pdf"),
            ("WorldCat ISBN record", "https://www.worldcat.org/isbn/9789294721938"),
        ],
    },
    {
        "title": "Кластерний аналіз використання та розповсюдження Інтернет-технологій у регіонах України",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2020,
        "journal_title": "Business Inform",
        "venue_display": "Business Inform",
        "volume": "3",
        "issue": "506",
        "doi": "10.32983/2222-4459-2020-3-244-252",
        "issn": "2222-4459",
        "first_page": "244",
        "last_page": "252",
        "lang": "uk",
        "links": [
            ("DOI record", "https://doi.org/10.32983/2222-4459-2020-3-244-252"),
            ("Publisher PDF", "https://www.business-inform.net/export_pdf/business-inform-2020-3_0-pages-244_252.pdf"),
            ("Publisher article page", "https://www.business-inform.net/article/?year=2020&abstract=2020_3_0_244_252&lang=en"),
        ],
    },
    {
        "title": "STATISTICAL ANALYSIS OF THE USE OF SOCIAL MEDIA IN EDUCATION AND TRAINING",
        "authors": ["O. Tumanov"],
        "citation_authors": ["Tumanov, O."],
        "year": 2020,
        "journal_title": "Agrosvit",
        "venue_display": "Agrosvit",
        "doi": "10.32702/2306-6792.2020.5.75",
        "issn": "2306-6792",
        "issue": "5",
        "first_page": "75",
        "last_page": "80",
        "lang": "en",
        "links": [
            ("DOI record", "https://doi.org/10.32702/2306-6792.2020.5.75"),
            ("Publisher PDF", "http://www.agrosvit.info/pdf/5_2020/13.pdf"),
            ("Publisher article page", "http://www.agrosvit.info/?op=1&z=3121&i=11"),
        ],
    },
    {
        "title": "Aspects of Using Social Media in Research",
        "authors": ["O. Tumanov"],
        "citation_authors": ["Tumanov, O."],
        "year": 2019,
        "journal_title": "Scientific Bulletin of the National Academy of Statistics, Accounting and Audit",
        "venue_display": "Scientific Bulletin of the National Academy of Statistics, Accounting and Audit",
        "doi": "10.31767/nasoa.4.2019.03",
        "issn": "2521-1323",
        "issue": "4",
        "first_page": "24",
        "last_page": "29",
        "lang": "en",
        "citations": 4,
        "links": [
            ("DOI record", "https://doi.org/10.31767/nasoa.4.2019.03"),
            ("Publisher PDF", "https://nasoa-journal.com.ua/index.php/journal/article/download/192/194"),
            ("Publisher article page", "https://nasoa-journal.com.ua/index.php/journal/article/view/192"),
        ],
    },
    {
        "title": "Social media as the object of statistical research",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2019,
        "journal_title": "Business Inform",
        "venue_display": "Business Inform",
        "volume": "12",
        "issue": "503",
        "doi": "10.32983/2222-4459-2019-12-8-14",
        "issn": "2222-4459",
        "first_page": "8",
        "last_page": "14",
        "lang": "en",
        "citations": 4,
        "links": [
            ("DOI record", "https://doi.org/10.32983/2222-4459-2019-12-8-14"),
            ("Publisher PDF", "https://www.business-inform.net/export_pdf/business-inform-2019-12_0-pages-8_14.pdf"),
            ("Publisher article page", "https://www.business-inform.net/article/?year=2019&abstract=2019_12_0_8_14&lang=en"),
        ],
    },
    {
        "title": "Інформаційне забезпечення статистичного вивчення соціальних медіа",
        "authors": ["T. H. Chala", "Oleksii O. Tumanov"],
        "citation_authors": ["Chala, T. H.", "Tumanov, Oleksii O."],
        "year": 2019,
        "journal_title": "The Problems of Economy",
        "venue_display": "The Problems of Economy",
        "volume": "4",
        "issue": "42",
        "doi": "10.32983/2222-0712-2019-4-239-249",
        "issn": "2222-0712",
        "first_page": "239",
        "last_page": "249",
        "lang": "uk",
        "citations": 2,
        "links": [
            ("DOI record", "https://doi.org/10.32983/2222-0712-2019-4-239-249"),
            ("Publisher PDF", "https://www.problecon.com/export_pdf/problems-of-economy-2019-4_0-pages-239_249.pdf"),
            ("Publisher article page", "https://www.problecon.com/article/?year=2019&abstract=2019_4_0_239_249"),
        ],
    },
    {
        "title": "Розвиток статистичної системи управління метаданими в Україні",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2019,
        "conference_title": "Priority directions of science development. Abstracts of the III International scientific and practical conference",
        "venue_display": "Priority directions of science development. Abstracts of the III International scientific and practical conference",
        "first_page": "832",
        "last_page": "834",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/01/priority-directions-of-science-development-iii.pdf"),
            ("Conference archive page", "https://sci-conf.com.ua/iii-mezhdunarodnaya-nauchno-prakticheskaya-konferencziya-priority-directions-of-science-development-28-29-dekabrya-2019-goda-helsinki-finlyandiya-arhiv/"),
        ],
    },
    {
        "title": "СТАТИСТИЧНИЙ АНАЛІЗ РІВНЯ РОЗВИТКУ ІНФОРМАЦІЙНОГО СУСПІЛЬСТВА В УКРАЇНІ",
        "authors": ["Oleksii O. Tumanov"],
        "citation_authors": ["Tumanov, Oleksii O."],
        "year": 2019,
        "conference_title": "Perspectives of world science and education. Abstracts of the XIII International scientific and practical conference",
        "venue_display": "Perspectives of world science and education. Abstracts of the XIII International scientific and practical conference",
        "first_page": "897",
        "last_page": "901",
        "lang": "uk",
        "links": [
            ("Proceedings PDF", "https://sci-conf.com.ua/wp-content/uploads/2020/06/PERSPECTIVES-OF-WORLD-SCIENCE-AND-EDUCATION_30-31.oct_.19.pdf"),
        ],
    },
    {
        "title": "Optimisation de la synchronisation de donnees entre les systemes informatiques avec l'utilisation des technologies nuageux",
        "authors": ["O. Tumanov"],
        "citation_authors": ["Tumanov, O."],
        "year": 2014,
        "lang": "fr",
        "links": [],
    },
]


def transliterate(text: str) -> str:
    normalized = text.translate(CYRILLIC_MAP)
    normalized = unicodedata.normalize("NFKD", normalized)
    return normalized.encode("ascii", "ignore").decode("ascii")


def slugify(text: str) -> str:
    ascii_text = transliterate(text)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def ensure_slugs() -> None:
    seen: dict[str, int] = {}
    for publication in PUBLICATIONS:
        base_slug = publication.get("slug") or slugify(publication["title"])
        count = seen.get(base_slug, 0)
        seen[base_slug] = count + 1
        publication["slug"] = base_slug if count == 0 else f"{base_slug}-{count + 1}"


def page_url(publication: dict) -> str:
    return f"{SITE_URL}{publication['slug']}.html"


def escape(text: str) -> str:
    return html.escape(text, quote=True)


def page_range(publication: dict) -> str | None:
    first_page = publication.get("first_page")
    last_page = publication.get("last_page")
    if first_page and last_page:
        return first_page if first_page == last_page else f"{first_page}-{last_page}"
    return None


def render_citation_line(publication: dict) -> str:
    parts = [escape(", ".join(publication["authors"]))]
    title = escape(publication["title"])
    title_suffix = "" if publication["title"].rstrip().endswith((".", "?", "!")) else "."
    parts.append(f"({publication['year']}). {title}{title_suffix}")

    venue = publication.get("venue_display")
    volume = publication.get("volume")
    issue = publication.get("issue")
    pages = page_range(publication)

    trailing_parts = []
    if volume and issue:
        trailing_parts.append(f"{escape(volume)} ({escape(issue)})")
    elif volume:
        trailing_parts.append(escape(volume))
    elif issue:
        trailing_parts.append(escape(issue))
    if pages:
        trailing_parts.append(escape(pages))

    if venue:
        venue_fragment = f"<em>{escape(venue)}</em>"
        if trailing_parts:
            venue_fragment += ", " + ", ".join(trailing_parts)
        venue_fragment += "."
        parts.append(venue_fragment)
    elif trailing_parts:
        parts.append(", ".join(trailing_parts) + ".")

    return " ".join(parts)


def meta_tags(publication: dict) -> str:
    tags = [
        ("citation_title", publication["title"]),
        ("citation_publication_date", str(publication["year"])),
        ("citation_abstract_html_url", page_url(publication)),
        ("citation_language", publication.get("lang", "en")),
    ]

    for author in publication.get("citation_authors", publication["authors"]):
        tags.append(("citation_author", author))

    if publication.get("journal_title"):
        tags.append(("citation_journal_title", publication["journal_title"]))
    if publication.get("conference_title"):
        tags.append(("citation_conference_title", publication["conference_title"]))
    if publication.get("issn"):
        tags.append(("citation_issn", publication["issn"]))
    if publication.get("volume"):
        tags.append(("citation_volume", publication["volume"]))
    if publication.get("issue"):
        tags.append(("citation_issue", publication["issue"]))
    if publication.get("first_page"):
        tags.append(("citation_firstpage", publication["first_page"]))
    if publication.get("last_page"):
        tags.append(("citation_lastpage", publication["last_page"]))
    if publication.get("doi"):
        tags.append(("citation_doi", publication["doi"]))

    for label, url in publication.get("links", []):
        if "pdf" in label.lower():
            tags.append(("citation_pdf_url", url))
            break

    return "\n".join(
        f'  <meta name="{escape(name)}" content="{escape(value)}">' for name, value in tags if value
    )


def structured_data(publication: dict) -> str:
    container_type = "Periodical" if publication.get("journal_title") else "CreativeWorkSeries"
    payload = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": publication["title"],
        "name": publication["title"],
        "url": page_url(publication),
        "datePublished": str(publication["year"]),
        "inLanguage": publication.get("lang", "en"),
        "author": [{"@type": "Person", "name": name} for name in publication["authors"]],
        "mainEntityOfPage": page_url(publication),
    }

    alternate_titles = publication.get("alternate_titles", [])
    if alternate_titles:
        payload["alternateName"] = alternate_titles[0] if len(alternate_titles) == 1 else alternate_titles

    venue = publication.get("venue_display")
    if venue:
        payload["isPartOf"] = {"@type": container_type, "name": venue}

    pagination = page_range(publication)
    if pagination:
        payload["pagination"] = pagination

    if publication.get("doi"):
        payload["identifier"] = {
            "@type": "PropertyValue",
            "propertyID": "DOI",
            "value": publication["doi"],
        }

    same_as = [url for _, url in publication.get("links", [])]
    if same_as:
        payload["sameAs"] = same_as

    description = build_summary(publication, short=True)
    if description:
        payload["description"] = description

    return json.dumps(payload, ensure_ascii=False, indent=2)


def build_summary(publication: dict, short: bool = False) -> str:
    if publication.get("abstract"):
        return publication["abstract"]

    authors = ", ".join(publication["authors"])
    venue = publication.get("venue_display")
    pages = page_range(publication)
    has_external_links = bool(publication.get("links"))
    citation_sentence = f"This page records the publication “{publication['title']}” by {authors}."
    if venue:
        citation_sentence += f" The public bibliographic record lists it in {venue} in {publication['year']}."
    else:
        citation_sentence += f" The public bibliographic record lists it in {publication['year']}."
    if pages:
        citation_sentence += f" Reported pagination: {pages}."

    if short:
        return citation_sentence

    notes = [
        citation_sentence,
        "This catalog page is maintained as a stable public reference for indexing and citation verification.",
    ]

    if has_external_links:
        notes.append("Verified publisher, DOI, or PDF links are included below when available.")
    else:
        notes.append("No public publisher PDF or article page has been verified for this record yet.")

    citations = publication.get("citations")
    if citations:
        notes.append(f"The public Google Scholar profile currently reports {citations} citation{'s' if citations != 1 else ''} for this work.")

    return " ".join(notes)


def discovery_links(publication: dict) -> list[tuple[str, str]]:
    scholar_queries = [f'"{publication["title"]}"']
    scholar_queries.extend(f'"{title}"' for title in publication.get("alternate_titles", []))
    scholar_query = urllib.parse.quote(" OR ".join(scholar_queries))
    return [
        ("Google Scholar search", f"https://scholar.google.com/scholar?q={scholar_query}"),
        ("ResearchGate profile", RESEARCHGATE_PROFILE_URL),
        ("ORCID profile", ORCID_PROFILE_URL),
    ]


def combined_links(publication: dict) -> list[tuple[str, str]]:
    combined: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for label, url in [*publication.get("links", []), *discovery_links(publication)]:
        key = (label, url)
        if key in seen:
            continue
        combined.append((label, url))
        seen.add(key)
    return combined


def render_links(publication: dict) -> str:
    links = combined_links(publication)
    if not links:
        return ""

    items = "\n".join(
        f'      <p><a href="{escape(url)}">{escape(label)}</a></p>' for label, url in links
    )
    return f"""    <section class="links">
      <h2>Links</h2>
{items}
    </section>"""


def render_notes(publication: dict) -> str:
    return f"""    <section class="abstract">
      <h2>Record Note</h2>
      <p>{escape(build_summary(publication))}</p>
    </section>
"""


def render_alternate_titles(publication: dict) -> str:
    alternate_titles = publication.get("alternate_titles", [])
    if not alternate_titles:
        return ""

    items = "\n".join(
        f'    <p class="meta">Also cited as: {escape(title)}</p>' for title in alternate_titles
    )
    return items + "\n"


def render_publication_page(publication: dict) -> str:
    title = escape(publication["title"])
    description_text = f"Publication record for {publication['title']} by {', '.join(publication['authors'])}."
    alternate_titles = publication.get("alternate_titles", [])
    if alternate_titles:
        description_text += f" Also cited as {alternate_titles[0]}."
    description = escape(description_text)
    citation_line = render_citation_line(publication)
    authors_display = escape(", ".join(publication["authors"]))
    doi = publication.get("doi")
    doi_line = f'    <p class="meta">DOI: {escape(doi)}</p>\n' if doi else ""

    return f"""<!doctype html>
<html lang="{escape(publication.get('lang', 'en'))}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{escape(page_url(publication))}">
{meta_tags(publication)}
  <script type="application/ld+json">
{structured_data(publication)}
  </script>
  <style>
    :root {{
      color-scheme: light;
      --bg: #fbf8f1;
      --text: #1d1a17;
      --muted: #6c6055;
      --accent: #8c2f1b;
      --border: #ddd2c5;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(140, 47, 27, 0.08), transparent 32%),
        linear-gradient(180deg, #f2ece2 0%, var(--bg) 100%);
    }}

    main {{
      max-width: 780px;
      margin: 0 auto;
      padding: 56px 20px 72px;
    }}

    h1 {{
      margin: 0 0 12px;
      font-size: 2.35rem;
      line-height: 1.1;
    }}

    h2 {{
      margin-top: 0;
    }}

    p {{
      line-height: 1.65;
    }}

    .authors,
    .citation,
    .meta {{
      color: var(--muted);
    }}

    .abstract,
    .links {{
      margin-top: 28px;
      padding: 22px 24px;
      background: rgba(255, 253, 248, 0.92);
      border: 1px solid var(--border);
      border-radius: 14px;
    }}

    a {{
      color: var(--accent);
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <main>
    <p><a href="index.html">All publications</a></p>
    <h1>{title}</h1>
    <p class="authors">{authors_display}</p>
    <p class="citation">{citation_line}</p>
{render_alternate_titles(publication)}\
{doi_line}{render_notes(publication)}
{render_links(publication)}
  </main>
</body>
</html>
"""


def render_index_item(publication: dict) -> str:
    links = [f'<a href="{escape(publication["slug"])}.html">Local page</a>']
    for label, url in combined_links(publication):
        links.append(f'<a href="{escape(url)}">{escape(label)}</a>')

    citation_hint = ""
    if publication.get("citations"):
        citation_hint = f' <span class="source-note">Cited by {publication["citations"]} on Google Scholar.</span>'

    return f"""          <div class="pub-entry">
            <h3><a href="{escape(publication["slug"])}.html">{escape(publication["title"])}</a></h3>
            <p class="meta">{render_citation_line(publication)}</p>
            <p class="links">{' '.join(links)}</p>
            <p class="source-note">Catalog page with citation metadata for indexing and verification.{citation_hint}</p>
          </div>"""


def render_collection_structured_data(publications: list[dict]) -> str:
    items = []
    for idx, publication in enumerate(publications, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": idx,
                "url": page_url(publication),
                "item": {
                    "@type": "ScholarlyArticle",
                    "name": publication["title"],
                    "datePublished": str(publication["year"]),
                    "author": [{"@type": "Person", "name": name} for name in publication["authors"]],
                },
            }
        )

    payload = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Oleksii Tumanov Publications",
        "url": SITE_URL,
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(publications),
            "itemListElement": items,
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_index(publications: list[dict]) -> str:
    catalog = "\n".join(render_index_item(publication) for publication in publications)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Oleksii Tumanov Publications</title>
  <meta name="description" content="Publication catalog for Oleksii Tumanov with article-level citation metadata and stable public links.">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{SITE_URL}">
  <script type="application/ld+json">
{render_collection_structured_data(publications)}
  </script>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f4efe7;
      --panel: rgba(255, 252, 247, 0.92);
      --text: #1e1814;
      --muted: #6a5c52;
      --accent: #8c2f1b;
      --accent-soft: #ead8cf;
      --border: #d8cbbd;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(140, 47, 27, 0.12), transparent 30%),
        linear-gradient(180deg, #efe8de 0%, var(--bg) 100%);
    }}

    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 52px 20px 72px;
    }}

    h1, h2 {{
      margin: 0;
      line-height: 1.1;
    }}

    h1 {{
      font-size: 2.7rem;
      margin-bottom: 10px;
    }}

    h2 {{
      font-size: 1.35rem;
      margin-bottom: 12px;
    }}

    p {{
      line-height: 1.65;
    }}

    a {{
      color: var(--accent);
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    .intro {{
      max-width: 820px;
      margin: 0 0 24px;
      color: var(--muted);
      font-size: 1.08rem;
    }}

    .card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 14px 30px rgba(31, 24, 20, 0.05);
    }}

    .hero {{
      margin-bottom: 22px;
    }}

    .hero strong {{
      color: var(--accent);
    }}

    .pub-entry h3 {{
      margin: 0 0 8px;
      font-size: 1.08rem;
      line-height: 1.3;
    }}

    .meta,
    .source-note {{
      color: var(--muted);
    }}

    .meta {{
      margin: 0 0 10px;
    }}

    .links {{
      margin: 10px 0 0;
    }}

    .links a {{
      margin-right: 12px;
      white-space: nowrap;
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>Publications</h1>
      <p class="intro">
        A public publication catalog for Oleksii Tumanov with <strong>{len(publications)}</strong> indexed entries,
        article-level citation metadata and stable URLs intended to improve general web discoverability.
      </p>
    </section>

    <article class="card">
      <p class="source-note">
        This catalog is intentionally plain and exact: title, author, venue, year, and stable links.
        Each publication has its own local page with scholarly meta tags so search engines can crawl a direct bibliographic record.
      </p>
{catalog}
    </article>
  </main>
</body>
</html>
"""


def render_sitemap(publications: list[dict]) -> str:
    pages = [SITE_URL] + [page_url(publication) for publication in publications]
    lastmod = dt.date.today().isoformat()
    body = "\n".join(
        f"  <url><loc>{html.escape(url)}</loc><lastmod>{lastmod}</lastmod></url>" for url in pages
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def render_robots() -> str:
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n"


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def build() -> None:
    ensure_slugs()
    publications = sorted(PUBLICATIONS, key=lambda item: (-item["year"], item["title"].lower()))

    for publication in publications:
        write_text(ROOT / f"{publication['slug']}.html", render_publication_page(publication))

    write_text(ROOT / "index.html", render_index(publications))
    write_text(ROOT / "sitemap.xml", render_sitemap(publications))
    write_text(ROOT / "robots.txt", render_robots())


if __name__ == "__main__":
    build()
