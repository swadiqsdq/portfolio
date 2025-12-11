var professions = [];
var objprojects = {};
document.addEventListener('DOMContentLoaded', function() {

    $.ajax({
        type: 'GET',
        url: '/?ajax=1',
        dataType: 'json',
        success: function(response) {
            // Example: update DOM
            professions = response.profile.professions
            objprojects = response.projects
            startTypingEffect();
            fnProjects(objprojects);
            
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', error);
        }
    });
    
    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        navLinks.classList.toggle('active');
    });
    
    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-links li a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
    
    // Sticky Header on Scroll
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        header.classList.toggle('sticky', window.scrollY > 0);
    });
    
    // Typing Animation
    const typedTextSpan = document.querySelector('.typed-text');
    const cursorSpan = document.querySelector('.cursor');

    function startTypingEffect(){
    
        // const textArray = ['Developer', 'Programmer', 'Backend Engineer', 'Django Specialist'];
        const textArray = professions
        const typingDelay = 200;
        const erasingDelay = 100;
        const newTextDelay = 2000; // Delay between current and next text
        let textArrayIndex = 0;
        let charIndex = 0;
        
        function type() {
            if (charIndex < textArray[textArrayIndex].length) {
                if(!cursorSpan.classList.contains('typing')) cursorSpan.classList.add('typing');
                typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
                charIndex++;
                setTimeout(type, typingDelay);
            } 
            else {
                cursorSpan.classList.remove('typing');
                setTimeout(erase, newTextDelay);
            }
        }
        
        function erase() {
            if (charIndex > 0) {
                if(!cursorSpan.classList.contains('typing')) cursorSpan.classList.add('typing');
                typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
                charIndex--;
                setTimeout(erase, erasingDelay);
            } 
            else {
                cursorSpan.classList.remove('typing');
                textArrayIndex++;
                if(textArrayIndex>=textArray.length) textArrayIndex=0;
                setTimeout(type, typingDelay + 1100);
            }
        }
        
        // Start the typing effect on load
        setTimeout(type, newTextDelay + 250);

    }
    
    // Tabs in About Section
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            
            tabBtns.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Portfolio Filter
    const filterBtns = document.querySelectorAll('.filter-btn');
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');
            
            const filter = btn.getAttribute('data-filter');
            
            portfolioItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
    
    // Portfolio Modal
    const portfolioItemsContainer = document.querySelector('.portfolio-grid');
    const portfolioModal = document.querySelector('.portfolio-modal');
    const modalImg = portfolioModal.querySelector('.modal-img');
    const modalTitle = portfolioModal.querySelector('.modal-title');
    const modalDescription = portfolioModal.querySelector('.modal-description');
    const modalTech = portfolioModal.querySelector('.modal-tech');
    const modalFeatures = portfolioModal.querySelector('.modal-features');
    const modalLink = portfolioModal.querySelector('.modal-link');
    const modalCode = portfolioModal.querySelector('.modal-code');
    const closeModal = portfolioModal.querySelector('.close-modal');
    
    // Project data for modal
    
    function fnProjects(projects) {
        portfolioItemsContainer.addEventListener('click', (e) => {
            const portfolioItem = e.target.closest('.portfolio-item');
            if (!portfolioItem) return;
            
            const title = portfolioItem.querySelector('h3').textContent;
            const project = projects[title];
            
            if (project) {
                modalImg.src = portfolioItem.querySelector('img').src;
                modalTitle.textContent = title;
                modalDescription.textContent = project.description;
                modalTech.innerHTML = project.tech.map(t => `<span>${t}</span>`).join('');
                
                // Add features to modal
                modalFeatures.innerHTML = `
                    <h4>Key Features:</h4>
                    <ul>
                        ${project.features.map(f => `<li>${f}</li>`).join('')}
                    </ul>
                `;
                
                modalLink.href = project.link;
                modalCode.href = project.code;
                
                portfolioModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });
        
    }
   
    closeModal.addEventListener('click', () => {
        portfolioModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    });
    
    portfolioModal.addEventListener('click', (e) => {
        if (e.target === portfolioModal) {
            portfolioModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
    
    // Contact Form Submission
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('form-message');
    
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Simulate form submission
        formMessage.textContent = 'Your message has been sent successfully!';
        formMessage.classList.remove('error');
        formMessage.classList.add('success');
        formMessage.style.display = 'block';
        
        // Reset form
        contactForm.reset();
        
        // Hide message after 5 seconds
        setTimeout(() => {
            formMessage.style.display = 'none';
        }, 5000);
    });
    
    // Back to Top Button
    const backToTopBtn = document.querySelector('.back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('active');
        } else {
            backToTopBtn.classList.remove('active');
        }
    });
    
    backToTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
   // Dark/Light Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('theme') || 'light';

// Set initial theme
document.documentElement.setAttribute('data-theme', currentTheme);
updateIcons(currentTheme);

themeToggle.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  updateIcons(newTheme);
  
  // Add animation
  themeToggle.classList.add('theme-change');
  setTimeout(() => {
    themeToggle.classList.remove('theme-change');
  }, 300);
});

function updateIcons(theme) {
  const lightIcon = document.querySelector('.light-icon');
  const darkIcon = document.querySelector('.dark-icon');
  
  if (theme === 'dark') {
    lightIcon.style.display = 'none';
    darkIcon.style.display = 'block';
  } else {
    lightIcon.style.display = 'block';
    darkIcon.style.display = 'none';
  }
}
    // Update copyright year
    document.getElementById('year').textContent = new Date().getFullYear();
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animate progress bars on scroll
    const progressBars = document.querySelectorAll('.progress');
    
    function animateProgressBars() {
        progressBars.forEach(bar => {
            const width = bar.style.width;
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
        });

        
    }
    
    // Intersection Observer for progress bars
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateProgressBars();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('.skill-category').forEach(category => {
        observer.observe(category);
    });
});

$('#btnIdSubmit').click(function (event) {
    event.preventDefault();

    let strName = $('#strIdName').val();
    let strEmail = $('#strIdEmail').val();
    let strSubject = $('#strIdSubject').val();
    let strMessage = $('#strIdMessage').val();

    
    if (strName !== '' && strEmail !== ''  && strMessage !== '') {
        fnSaveContact(strName, strEmail, strSubject, strMessage);
    } else {
        $('#form-message')
            .text('Please enter the field before submitting.')
            .removeClass('success')
            .addClass('error')
            .fadeIn();
    }
    
    
});

function fnSaveContact(name, email, subject, message) {
    $.ajax({
        url: "/contact/",
        type: "POST",
        data: {
            name: name,
            email: email,
            subject: subject,
            message: message,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            // Clear inputs
            $('#strIdName').val('');
            $('#strIdEmail').val('');
            $('#strIdSubject').val('');
            $('#strIdMessage').val('');
            console.log("Saved Successfully", response);
             // Show success message
            $('#form-message')
                .text('Your message has been sent successfully!')
                .removeClass('error')
                .addClass('success')
                .fadeIn();

            // Reset form
            $('#contactForm')[0].reset();

            // Hide message after 5 seconds
            setTimeout(() => {
                $('#form-message').fadeOut();
            }, 5000);
        },
        error: function (xhr) {
            console.log("Error:", xhr.responseText);
            $('#form-message')
                .text('Something went wrong. Please try again.')
                .removeClass('success')
                .addClass('error')
                .fadeIn();
        }
    });
}

let lastScrollTop = 0;
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', function () {
    let currentScroll = window.pageYOffset;

    if (currentScroll > lastScrollTop) {
        // Scrolling down → hide
        navbar.style.top = "-80px";   // Adjust height if your navbar is bigger
    } else {
        // Scrolling up → show
        navbar.style.top = "0";
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});