# 🎸 Riff Rush

**Riff Rush** é um jogo de ritmo musical de navegador (inspirado em clássicos de guitarra arcade), desenvolvido para funcionar com teclado ou botões físicos mapeados via USB (`12534` e `ABECD`), com suporte a **1 ou 2 jogadores**, **detecção automática de batidas/notas** a partir de qualquer arquivo de áudio ou link do YouTube, **notas longas (sustain)**, **acordes** e **ajuste de sincronia em tempo real**.

🔗 **Jogue online (GitHub Pages):** [https://victoriazambomg.github.io/Riff-Rush/](https://victoriazambomg.github.io/Riff-Rush/)

---

## 🎮 Como Jogar

### Controles e Cores das Pistas
As 5 pistas seguem a sequência exata de cores e teclas abaixo (da esquerda para a direita):

| Pista | Cor | Jogador 1 (Números) | Jogador 2 (Letras) |
| :---: | :--- | :---: | :---: |
| **1** | 🔴 Vermelho | `1` | `A` |
| **2** | 🟡 Amarelo | `2` | `B` |
| **3** | ⚪ Branco | `5` | `E` |
| **4** | 🟢 Verde | `3` | `C` |
| **5** | 🔵 Azul | `4` | `D` |

* **Modo 1 Jogador:** Você pode usar tanto `1 2 5 3 4` quanto `A B E C D`.
* **Modo 2 Jogadores:** Tela dividida lado a lado — **Jogador 1** usa `1 2 5 3 4` e **Jogador 2** usa `A B E C D`.
* **Atalhos durante a partida:**
  * `⬅️` / `➡️` (Setas): Ajusta a sincronia do áudio em `-10 ms` / `+10 ms` em tempo real.
  * `ESC`: Volta para o menu principal.

### Mecânicas de Pontuação
* **Notas Simples:** Aperte a tecla quando a nota atingir o círculo na linha de acerto (`PERFEITO! = 100 pts`, `ÓTIMO = 70 pts`, `BOM = 40 pts`).
* **Acordes (2 notas simultâneas):** Aperte as duas teclas correspondentes ao mesmo tempo (presente nos modos *Médio* e *Difícil*).
* **Notas Longas (Segurar / Sustain):** Mantenha a tecla pressionada até o final da cauda da nota para ganhar pontos contínuos com efeito de vibrato e um bônus de `+50 pts × multiplicador` ao completar (`SEGUROU!`).
* **Multiplicador:** A cada 10 acertos seguidos, o multiplicador sobe (`x1` → `x2` → `x3` → `x4`). Errar uma nota ou apertar no vazio zera o combo.

---

## 🚀 Como Rodar e Replicar o Projeto Localmente

Você pode jogar de **duas formas**:

### Opção 1: Apenas o Jogo (Sem instalação / GitHub Pages)
Basta abrir o arquivo `index.html` diretamente no navegador (ou acessar o link do GitHub Pages).
* Funciona 100% no navegador para o **modo de batida eletrônica** e para carregar **arquivos de áudio locais (`MP3`, `OGG`, `WAV`)**.

### Opção 2: Com Suporte a Links do YouTube (Servidor Local em Python)
Como os navegadores bloqueiam a leitura direta de áudio do YouTube por segurança (CORS), o projeto inclui um mini-servidor em Python (`server.py`) que baixa e fornece o áudio para o analisador rítmico do jogo.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/victoriazambomg/Riff-Rush.git
   cd Riff-Rush
   ```
2. **Instale as dependências do Python (`Flask` e `yt-dlp`):**
   ```bash
   pip install flask yt-dlp
   ```
3. **Inicie o jogo:**
   * **No Windows:** Dê dois cliques em `iniciar_jogo.bat`
   * **Ou pelo terminal:**
     ```bash
     python server.py
     ```
4. Acesse **`http://localhost:5000`** no navegador, cole qualquer link do YouTube, clique em **Carregar** e escolha a dificuldade!

---

## 🤖 Prompt Único para Recriar este Jogo do Zero

Se você quiser gerar exatamente este projeto do zero em uma IA de programação em uma única tentativa, copie e cole o prompt abaixo:

```text
Crie um jogo completo de ritmo estilo arcade chamado "Riff Rush" em HTML5 Canvas + Web Audio API (em um único arquivo index.html) acompanhado de um mini-servidor Python (server.py com Flask e yt-dlp) e um script iniciar_jogo.bat para Windows.

Especificações obrigatórias do jogo:

1. CONTROLES E CORES DAS 5 PISTAS:
- Ordem obrigatória das cores das 5 pistas/botões (da esquerda para a direita):
  1ª Vermelho (#e74c3c), 2ª Amarelo (#f1c40f), 3ª Branco (#ffffff com contorno cinza para contraste), 4ª Verde (#2ecc71), 5ª Azul (#3498db).
- Mapeamento obrigatório das teclas na ordem das 5 pistas:
  - Números: ['1', '2', '5', '3', '4']
  - Letras:  ['a', 'b', 'e', 'c', 'd']
- Modo 1 Jogador: aceita tanto 12534 quanto ABECD.
- Modo 2 Jogadores: duas pistas lado a lado com o mesmo mapa de notas; Jogador 1 usa 12534 e Jogador 2 usa ABECD. Ao final, mostre uma coroa (👑) para o vencedor.

2. IDENTIDADE VISUAL E MENU:
- Tema inteiro em tons de vinho escuro (#260917, #360d20, #52132e) e rosa claro (#f48fb1, #f8bbd0, #fce4ec), com exceção das 5 cores dos botões/notas.
- O menu inicial e a tela de fim de jogo devem ter design flat moderno e limpo, sem efeitos de LED/neon (sem box-shadow/drop-shadow) e sem degradês (apenas cores sólidas e bordas discretas).
- Durante a partida (no Canvas), inclua efeitos visuais ricos: partículas de explosão ao acertar, anéis expansivos, feixe de luz ao apertar a pista, chamas laterais quando o multiplicador estiver em x4, tremor de tela em combos altos/erros e estrelas caindo ao fundo.

3. MÚSICAS (YOUTUBE, ARQUIVO LOCAL E MODO SINTETIZADO) E SINCRONIA:
- No menu, permita:
  a) Colar um link do YouTube (que chama GET /api/youtube?url=... no server.py com yt-dlp, faz cache em yt_cache/ e retorna o áudio decodificado pelo Web Audio API).
  b) Escolher um arquivo de áudio local (MP3/OGG/WAV).
  c) Jogar sem música carregada (gera notas procedurais com batida eletrônica sintetizada de bumbo/chimbal e notas musicais em escala pentatônica).
- Algoritmo de detecção e sincronia de áudio (genChartFromAudio):
  - Use resolução de hop = 256 amostras, filtro passa-baixa (~160 Hz) para destacar bumbo/baixo combinado com fluxo de energia total e interpolação parabólica de picos.
  - Calcule automaticamente o BPM dominante (85–165 BPM) por autocorrelação dos ataques fortes e encontre a fase (beatOffset) da batida.
  - Quantize suavemente as notas detectadas para a grade de 1/4 de batida e alinhe as linhas de batida da pista com o BPM/fase reais.
  - Separe as notas nas 5 pistas de acordo com os quantis da taxa de cruzamento por zero (sons graves à esquerda, agudos à direita).
- Inclua um controle deslizante de "Sincronia de áudio" (-250 ms a +250 ms) no menu e permita ajustar em tempo real durante o jogo com as setas Esquerda/Direita.

4. CALIBRAGEM DE DIFICULDADE, ACORDES E NOTAS SEGURADAS (SUSTAIN):
- 3 dificuldades calibradas:
  - Fácil:   speed = 190 px/s, intervalo mínimo entre notas (MIN_GAP) = 0.85s, sem acordes.
  - Médio:   speed = 275 px/s, MIN_GAP = 0.52s, chance moderada de acordes (2 notas juntas).
  - Difícil: speed = 410 px/s, MIN_GAP = 0.33s, mais notas e acordes.
- Janelas de acerto: Perfeito (60ms = 100 pts), Ótimo (110ms = 70 pts), Bom (160ms = 40 pts).
- Notas de segurar (sustain): quando houver espaço livre >= 0.8s até a próxima nota, transforme parte das notas em sustains com cauda longa. Enquanto o jogador segura a tecla, toque um som contínuo com vibrato (LFO), ondule a cauda visualmente, some pontos por segundo e dê um bônus de +50 × multiplicador ao segurar até o fim ("SEGUROU!").
```
