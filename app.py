from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

profile = {
    "name": "Safa Tiara Sutrisno",
    "title": "Mahasiswa Teknologi Rekayasa Sistem Elektronika",
    "subtitle": "D4 Teknologi Rekayasa Sistem Elektronika · Politeknik Caltex Riau",
    "tagline": "Fokus pada pengembangan sistem tertanam (embedded systems), instrumentasi elektronik, dan teknologi Internet of Things (IoT) untuk masa depan inovatif.",
    "email": "safa24trse@mahasiswa.pcr.ac.id",
    "phone": "082160353366",
    "location": "Pekanbaru, Riau",
    "photo": "profile.jpg",
    "cv_file": "CV_Safa_Tiara_Sutrisno.pdf",
    "motto": '"Ilmu tanpa amal seperti pohon tanpa buah — ia tumbuh menjulang, namun tidak memberikan keteduhan dan manfaat bagi sekitarnya."',
    "about": (
        "Halo! Saya Safa Tiara Sutrisno, mahasiswa semester 4 Program Studi "
        "Teknologi Rekayasa Sistem Elektronika di Politeknik Caltex Riau. "
        "Saya memiliki ketertarikan mendalam pada pengembangan hardware elektronik, "
        "otomasi industri, robotics, dan ekosistem Internet of Things (IoT). "
        "Melalui latar belakang pendidikan vokasi, saya terbiasa melakukan analisis sirkuit, "
        "perancangan PCB, hingga implementasi kode pemrograman pada mikrokontroler. "
        "Selain fokus di area teknis, saya aktif mengasah soft-skills kepemimpinan dan manajemen organisasi "
        "melalui peran strategis di lembaga legislatif dan eksekutif mahasiswa. Saya berkomitmen untuk "
        "mengintegrasikan keahlian teknik dan kemampuan manajerial guna menciptakan solusi teknologi yang aplikatif."
    ),
    "social": {
        "linkedin": "https://linkedin.com/in/safa-tiara",
        "github": "https://github.com/safatiara",
        "instagram": "https://instagram.com/safatiara_",
    },
}

education = [
    {"level": "Perguruan Tinggi", "name": "Politeknik Caltex Riau", "prodi": "D4 Teknologi Rekayasa Sistem Elektronika", "year": "2024 – Sekarang", "icon": "🎓"},
    {"level": "SMA", "name": "SMAN 3 Pekanbaru", "prodi": "MIPA", "year": "2021 – 2024", "icon": "🏫"},
    {"level": "SMP", "name": "MTS IT Al-Ittihadiyah", "prodi": "", "year": "2018 – 2021", "icon": "📚"},
    {"level": "SD", "name": "SDN 59 Pekanbaru", "prodi": "", "year": "2012 – 2018", "icon": "✏️"},
    {"level": "TK", "name": "TK Anamiroh", "prodi": "", "year": "2010 – 2012", "icon": "🌱"},
]

skills = {
    "Technical Skills": [
        "Pemrograman C / C++ (Arduino IDE)",
        "Mikrokontroler AVR & ESP32",
        "Desain Rangkaian Elektronika",
        "Perancangan PCB (EasyEDA / Altium)",
        "Internet of Things (Sensor Integration)",
        "Troubleshooting Hardware & Otomasi",
        "Python Programming (Basic)"
    ],
    "Design & Media": [
        "Canva Pro for Branding",
        "Visual Content Design",
        "Dokumentasi & Publikasi Acara",
        "Desain Grafis Dasar",
        "UI Layout Draft (Figma Basic)"
    ],
    "Tools & Software": [
        "Proteus Circuit Simulation",
        "Arduino IDE Suite",
        "VS Code Editor",
        "Microsoft Office Suite",
        "Git & GitHub Version Control"
    ]
}

projects = [
    {
        "title": "Smart Monitoring Suhu & Kelembaban",
        "desc": "Sistem monitoring industri berbasis ESP8266 yang mengirimkan data sensor DHT11 ke cloud dan menampilkannya secara real-time pada dashboard web interaktif.",
        "tags": ["IoT", "ESP8266", "Sensor", "Web Dashboard"]
    },
    {
        "title": "Robot Line Follower Berkecepatan Tinggi",
        "desc": "Rancang bangun robot pembaca jalur otomatis menggunakan array sensor inframerah dengan sistem kendali algoritma PID untuk pergerakan yang presisi.",
        "tags": ["Robotika", "Arduino", "PID Control", "Hardware"]
    },
    {
        "title": "Sistem Gate Otomatis berbasis RFID",
        "desc": "Prototipe sistem keamanan dan absensi presensi menggunakan modul RFID RC522, motor servo, dan verifikasi status lewat indikator LCD I2C.",
        "tags": ["Security", "RFID", "Embedded System"]
    },
    {
        "title": "Sistem Deteksi Dini Kebakaran",
        "desc": "Perancangan modul alarm keselamatan menggunakan integrasi sensor asap MQ-2 dan sensor panas yang memicu output alarm buzzer otomatis.",
        "tags": ["Safety System", "Sensors", "Electronics"]
    },
]

organization = [
    {
        "org": "Himpunan Mahasiswa Teknik Elektronika (HIMIKA)",
        "role": "Pengurus Organisasi",
        "period": "T.P 2025/2026",
        "place": "Politeknik Caltex Riau"
    },
    {
        "org": "Badan Legislatif Mahasiswa (BLM)",
        "role": "Sekretaris Umum",
        "period": "T.P 2025/2026",
        "place": "Politeknik Caltex Riau"
    },
]

committee = [
    {"event": "Diklat Administrasi Tingkat Kampus", "role": "Pemateri / Pembicara", "date": "12 Oktober 2025", "place": "Politeknik Caltex Riau"},
    {"event": "Pelatihan Nasional Internet of Things", "role": "Ketua Pelaksana", "date": "13 September 2025", "place": "Politeknik Caltex Riau"},
    {"event": "Kepanitiaan Kompetisi RoboSumo", "role": "Anggota Divisi Teknis", "date": "2 Agustus 2025", "place": "Politeknik Caltex Riau"},
    {"event": "Seminar Akbar Legislatif Mahasiswa", "role": "Anggota Pelaksana", "date": "9 November 2025", "place": "Politeknik Caltex Riau"},
    {"event": "Workshop Keterampilan Robotic", "role": "Anggota Komite", "date": "12 Oktober 2024", "place": "Politeknik Caltex Riau"},
]

achievements = [
    {"title": "Ketua Pelaksana Sukses - Pelatihan IoT", "desc": "Mengkoordinasi seluruh divisi dan mengelola jalannya pelatihan IoT tingkat dasar hingga menengah yang diikuti puluhan peserta.", "year": "2025"},
    {"title": "Pemateri Utama Diklat Administrasi", "desc": "Dipercaya menyusun materi sekaligus menjadi instruktur tata kelola dokumen formal organisasi untuk perwakilan mahasiswa.", "year": "2025"},
    {"title": "Sekretaris Umum Badan Legislatif Mahasiswa", "desc": "Mengarsip, menyusun regulasi administrasi, dan mengkoordinasi komunikasi birokrasi internal di ranah BLM PCR.", "year": "2025"},
]

hobbies = [
    {"name": "Robotika & DIY Electronics", "desc": "Bereksperimen membuat rangkaian sirkuit custom dan menguji modul sensor baru."},
    {"name": "Pengembangan Kode (Coding)", "desc": "Mempelajari logika pemrograman mikrokontroler dan optimasi script program."},
    {"name": "Desain Grafis Media", "desc": "Membuat layout poster publikasi dan aset visual kreatif untuk media informasi."},
    {"name": "Membaca Buku Edukasi", "desc": "Mengeksplorasi literatur teknologi terbaru serta jurnal pengembangan kapasitas diri."}
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=profile,
        education=education,
        skills=skills,
        projects=projects,
        organization=organization,
        committee=committee,
        achievements=achievements,
        hobbies=hobbies,
    )

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name", "").strip()
    if not name or not data.get("email") or not data.get("message"):
        return jsonify({"success": False, "msg": "Semua field wajib diisi."})
    return jsonify({"success": True, "msg": f"Terima kasih {name}! Pesan berhasil dikirim (Dummy)."})

if __name__ == "__main__":
    app.run(debug=True)