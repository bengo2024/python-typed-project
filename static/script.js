// Éléments DOM
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const refreshBtn = document.getElementById('refresh-errors');
const resetBtn = document.getElementById('reset-chat');
const autofixBtn = document.getElementById('autofix-btn');
const autofixModal = document.getElementById('autofix-modal');
const errorsSummary = document.getElementById('errors-summary');
const mypyErrors = document.getElementById('mypy-errors');
const ruffErrors = document.getElementById('ruff-errors');

// État
let isLoading = false;

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    loadErrors();
    
    // Auto-resize du textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = userInput.scrollHeight + 'px';
    });
    
    // Envoyer avec Entrée (Shift+Entrée pour nouvelle ligne)
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});

// Événements
sendBtn.addEventListener('click', sendMessage);
refreshBtn.addEventListener('click', loadErrors);
resetBtn.addEventListener('click', resetConversation);
autofixBtn.addEventListener('click', triggerAutofix);

// Charger les erreurs
async function loadErrors() {
    try {
        const response = await fetch('/api/errors');
        const errors = await response.json();
        
        // Mettre à jour le résumé
        errorsSummary.textContent = errors.summary;
        
        // Mettre à jour les détails
        mypyErrors.textContent = errors.mypy || 'Aucune erreur MyPy détectée ✅';
        ruffErrors.textContent = errors.ruff || 'Aucune erreur Ruff détectée ✅';
        
    } catch (error) {
        console.error('Erreur lors du chargement des erreurs:', error);
        errorsSummary.textContent = '❌ Erreur lors du chargement des erreurs';
    }
}

// Envoyer un message
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message || isLoading) return;
    
    // Ajouter le message de l'utilisateur
    addMessage(message, 'user');
    
    // Réinitialiser l'input
    userInput.value = '';
    userInput.style.height = 'auto';
    
    // Afficher le loader
    isLoading = true;
    const loaderId = addMessage('...', 'bot', true);
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        
        // Supprimer le loader
        document.getElementById(loaderId)?.remove();
        
        if (data.error) {
            addMessage(`❌ Erreur: ${data.error}`, 'bot');
        } else {
            addMessage(data.message, 'bot');
            
            // Mettre à jour les erreurs si disponibles
            if (data.errors) {
                errorsSummary.textContent = data.errors.summary;
                mypyErrors.textContent = data.errors.mypy || 'Aucune erreur MyPy détectée ✅';
                ruffErrors.textContent = data.errors.ruff || 'Aucune erreur Ruff détectée ✅';
            }
        }
        
    } catch (error) {
        document.getElementById(loaderId)?.remove();
        addMessage(`❌ Erreur de connexion: ${error.message}`, 'bot');
    } finally {
        isLoading = false;
    }
}

// Ajouter un message au chat
function addMessage(text, sender, isLoader = false) {
    const messageId = 'msg-' + Date.now();
    const messageDiv = document.createElement('div');
    messageDiv.id = messageId;
    messageDiv.className = `message ${sender}-message`;
    
    const avatar = sender === 'user' ? '👤' : '🤖';
    const time = new Date().toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
    
    // Convertir le markdown basique en HTML
    let formattedText = text;
    
    // Code blocks
    formattedText = formattedText.replace(/```([\s\S]*?)```/g, '<pre>$1</pre>');
    
    // Bold
    formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Listes
    formattedText = formattedText.replace(/^- (.+)$/gm, '<li>$1</li>');
    if (formattedText.includes('<li>')) {
        formattedText = formattedText.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');
    }
    
    // Paragraphes
    const paragraphs = formattedText.split('\n\n');
    formattedText = paragraphs.map(p => {
        if (!p.startsWith('<') && p.trim()) {
            return `<p>${p}</p>`;
        }
        return p;
    }).join('');
    
    messageDiv.innerHTML = `
        <div class="message-avatar">${avatar}</div>
        <div class="message-content">
            <div class="message-text ${isLoader ? 'loading' : ''}">
                ${formattedText}
            </div>
            <div class="message-time">${time}</div>
        </div>
    `;
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageId;
}

// Réinitialiser la conversation
async function resetConversation() {
    if (!confirm('Voulez-vous vraiment réinitialiser la conversation ?')) {
        return;
    }
    
    try {
        await fetch('/api/reset', { method: 'POST' });
        
        // Vider le chat sauf le message de bienvenue
        const messages = chatMessages.querySelectorAll('.message');
        messages.forEach((msg, index) => {
            if (index > 0) msg.remove();
        });
        
        addMessage('✅ Conversation réinitialisée ! Posez-moi une nouvelle question.', 'bot');
        
    } catch (error) {
        addMessage(`❌ Erreur lors de la réinitialisation: ${error.message}`, 'bot');
    }
}

// Déclencher l'auto-fix
async function triggerAutofix() {
    if (!confirm('Voulez-vous lancer l\'auto-fix ?\n\nCela va créer une nouvelle branche avec les corrections automatiques.')) {
        return;
    }
    
    // Afficher le modal
    autofixModal.classList.add('active');
    
    try {
        const response = await fetch('/api/autofix', { method: 'POST' });
        const data = await response.json();
        
        // Masquer le modal
        autofixModal.classList.remove('active');
        
        // Afficher le résultat dans le chat
        addMessage(data.message, 'bot');
        
        if (data.success && data.branch) {
            addMessage(
                `🔗 Pour créer une Pull Request, allez sur GitHub :\n\nhttps://github.com/bengo2024/python-typed-project/compare/${data.branch}`,
                'bot'
            );
        }
        
        // Recharger les erreurs
        setTimeout(loadErrors, 1000);
        
    } catch (error) {
        autofixModal.classList.remove('active');
        addMessage(`❌ Erreur lors de l'auto-fix: ${error.message}`, 'bot');
    }
}

// Suggestions rapides (optionnel)
const quickSuggestions = [
    "Quelles sont les erreurs actuelles ?",
    "Explique-moi l'erreur MyPy",
    "Explique-moi l'erreur Ruff",
    "Comment corriger ces erreurs ?",
    "Qu'est-ce qu'une annotation de type ?"
];

// Ajouter des suggestions au clic (optionnel)
function addQuickSuggestions() {
    const hintsDiv = document.querySelector('.input-hints');
    quickSuggestions.forEach(suggestion => {
        const btn = document.createElement('button');
        btn.textContent = suggestion;
        btn.className = 'suggestion-btn';
        btn.onclick = () => {
            userInput.value = suggestion;
            sendMessage();
        };
        hintsDiv.appendChild(btn);
    });
}

