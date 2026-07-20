const API_BASE_URL = 'http://127.0.0.1:8000';

function formatMediaUrl(url) {
    if (!url) return '';
    if (url.startsWith('http://') || url.startsWith('https://')) {
        return url;
    }
    return API_BASE_URL + url;
}

document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Load site settings & footer social links
    fetch(`${API_BASE_URL}/api/site-settings/`)
        .then(res => res.json())
        .then(data => {
            if (data.site_settings) {
                const addrEl = document.getElementById('footer-address');
                const phoneEl = document.getElementById('footer-phone');
                const emailEl = document.getElementById('footer-email');

                if (addrEl) addrEl.textContent = data.site_settings.address || 'Temple Road, Holy City';
                if (phoneEl) phoneEl.textContent = data.site_settings.phone || '+91 98765 43210';
                if (emailEl) emailEl.textContent = data.site_settings.email || 'info@kalyaneshwari.org';
            }

            if (data.social_links && data.social_links.length > 0) {
                const socialContainer = document.getElementById('footer-social-links');
                if (socialContainer) {
                    socialContainer.innerHTML = data.social_links.map(link => `
                        <a href="${link.url}" target="_blank" rel="noopener" title="${link.platform}">
                            <i class="${link.icon_class}"></i>
                        </a>
                    `).join('');
                }
            }
        })
        .catch(err => console.log('Site settings fetch error:', err));
});
