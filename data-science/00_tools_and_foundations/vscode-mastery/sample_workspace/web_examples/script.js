/**
 * VS Code Practice - Sample JavaScript File
 * ==========================================
 * Practice JavaScript editing, IntelliSense, and debugging
 */

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Form submission handler
const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        // Validation
        if (!name || !email || !message) {
            alert('Please fill in all fields');
            return;
        }

        // Simulate form submission
        console.log('Form submitted:', { name, email, message });
        alert('Thank you for your message, ' + name + '!');
        form.reset();
    });
}

// Feature card animations
const featureCards = document.querySelectorAll('.feature-card');
featureCards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
});

// Example function for debugging practice
function calculateSum(a, b) {
    // Set breakpoint here to practice debugging
    const result = a + b;
    console.log(`${a} + ${b} = ${result}`);
    return result;
}

// Practice IntelliSense - try typing "document." or "console."
function demonstrateIntelliSense() {
    // Type "document." and see IntelliSense suggestions
    document.title = 'VS Code Practice';

    // Type "console." and see available methods
    console.log('Practicing IntelliSense');
    console.table({ name: 'VS Code', type: 'Editor' });
}

// Array manipulation examples
const fruits = ['apple', 'banana', 'cherry', 'date'];

fruits.forEach(fruit => {
    console.log(fruit.toUpperCase());
});

// Object examples for IntelliSense practice
const user = {
    name: 'VS Code Learner',
    skills: ['JavaScript', 'Python', 'HTML', 'CSS'],
    level: 'Intermediate',
    getInfo: function() {
        return `${this.name} - ${this.level}`;
    }
};

// Practice debugging this function
function findMax(numbers) {
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }
    return max;
}

// Test the function
const testNumbers = [23, 45, 12, 67, 34, 89, 15];
const maxNumber = findMax(testNumbers);
console.log('Maximum number:', maxNumber);

// Export for testing (if using modules)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        calculateSum,
        findMax
    };
}
