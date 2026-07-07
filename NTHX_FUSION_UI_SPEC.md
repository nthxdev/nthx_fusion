# NTHX Fusion 0.1.0 — Complete UI/UX Specification
**Professional Product Design for Gradio Implementation**

---

## 🎨 DESIGN SYSTEM

### Color Palette
```
Primary Background:    #1a1a1a (near-black)
Secondary Background:  #2a2a2a (dark card)
Tertiary Background:   #3a3a3a (hover state)
Accent Color:          #ff4444 (red, selections/active)
Accent Hover:          #ff5555 (lighter red)
Text Primary:          #ffffff (white, labels)
Text Secondary:        #cccccc (gray, descriptions)
Text Tertiary:         #999999 (disabled/helper)
Border:                #444444 (dividers)
Success:               #44aa44 (green, completion)
Warning:               #ffaa00 (orange, alerts)
Info:                  #4488ff (blue, info messages)
```

### Typography
- **Font Family**: Inter, Roboto, -apple-system, sans-serif (system fonts)
- **Labels**: 12px, 600 weight, uppercase letter-spacing 0.5px
- **Body**: 14px, 400 weight
- **Headings**: 16px, 600 weight
- **Small text**: 11px, 400 weight

### Spacing & Layout
- **Base unit**: 8px
- **Container padding**: 16px
- **Section gap**: 12px
- **Component gap**: 8px
- **Border radius**: 4px (sharp, professional)

---

## 📐 MAIN LAYOUT STRUCTURE

```
┌─────────────────────────────────────────────────────────┐
│  HEADER: NTHX Fusion 0.1.0 Logo / Title                │
└─────────────────────────────────────────────────────────┘
┌──────────────────┬──────────────────┬──────────────────┐
│   SECTION 1      │   SECTION 2      │   SECTION 3      │
│   LEFT PANEL     │   CENTER PANEL   │   RIGHT PANEL    │
│   (Settings)     │   (Media Picker) │   (Preview/Logs) │
│   40% width      │   30% width      │   30% width      │
└──────────────────┴──────────────────┴──────────────────┘
```

---

## 🔧 COMPONENT SPECIFICATIONS

### 1️⃣ PROCESSOR SELECTOR (Radio Button Grid)

**Type**: Radio Button Group (exclusive selection)  
**Location**: Left Panel, Top (below media input section)  
**Display**: Grid layout, 2 columns  
**Default**: face_swapper selected  

**Processors to Display**:
- face_swapper (default selected)
- face_enhancer
- frame_enhancer
- face_detection
- face_selection
- masking
- age_modifier
- expression_restorer
- background_remover
- deep_swapper
- face_editor
- face_debugger
- frame_colorizer
- lip_syncer
(Add more as installed)

**Visual Design**:
```
┌─ PROCESSORS ─────────────────────────────────────────┐
│ ┌────────────────────┬────────────────────┐          │
│ │ ✓ face_swapper    │   face_enhancer    │          │
│ │ [RED BG]          │ [DARK BG]          │          │
│ └────────────────────┴────────────────────┘          │
│ ┌────────────────────┬────────────────────┐          │
│ │   frame_enhancer   │ face_detection     │          │
│ └────────────────────┴────────────────────┘          │
└──────────────────────────────────────────────────────┘
```

**Behavior**:
- **Unselected button**: Dark background (#2a2a2a), white text, 1px border #444444
- **Selected button**: Red background (#ff4444), white text, white checkmark icon top-left
- **Hover (unselected)**: Background #3a3a3a
- **Hover (selected)**: Background #ff5555
- **Click**: Instantly updates all dependent UI sections (processor-specific settings appear/hide)
- **Transition**: 150ms fade-in for new settings panel
- **Action**: Selecting a processor triggers refresh of the center/right panel settings

---

### 2️⃣ PROCESSOR-SPECIFIC SETTINGS PANELS (Collapsible Sections)

**Type**: Vertical scrollable container with accordion sections  
**Location**: Left Panel, Below Processor Selector  
**Behavior**: Only show settings for selected processor + global settings  

**Sections** (Dynamic based on selected processor):

#### FACE SWAPPER Settings:
```
┌─ FACE SWAPPER MODEL ──────────────────────────────────┐
│ [Dropdown: hyperswap_1a_256 ▼]                        │
│  └─ Shows: "Model not downloaded" status (if missing) │
└──────────────────────────────────────────────────────┘
┌─ FACE SWAPPER PIXEL BOOST ──────────────────────────┐
│ [Dropdown: 256x256 ▼]                                │
└──────────────────────────────────────────────────────┘
┌─ FACE SWAPPER WEIGHT ─────────────────────────────────┐
│ [Slider: 0.5 ────●────────── | ] 1.0                 │
│           0.0             ↑   Input: 0.5              │
│  └─ Link icon (lock/unlock for batch)                │
└──────────────────────────────────────────────────────┘
```

#### FACE ENHANCER Settings:
```
┌─ FACE ENHANCER MODEL ──────────────────────────────────┐
│ [Dropdown: gfpgan_1.4 ▼]                              │
└──────────────────────────────────────────────────────┘
┌─ FACE ENHANCER WEIGHT ────────────────────────────────┐
│ [Slider: 0.7 ────────────●── | ] 1.0                 │
│           0.0            ↑    Input: 0.7              │
└──────────────────────────────────────────────────────┘
```

#### FRAME ENHANCER Settings:
```
┌─ FRAME ENHANCER MODEL ────────────────────────────────┐
│ [Dropdown: realesrgan_x2plus ▼]                       │
└──────────────────────────────────────────────────────┘
```

#### FACE DETECTION Settings:
```
┌─ FACE DETECTOR MODEL ─────────────────────────────────┐
│ [Dropdown: yolo_face ▼]                               │
└──────────────────────────────────────────────────────┘
┌─ FACE DETECTOR SIZE ──────────────────────────────────┐
│ [Dropdown: 640x640 ▼]                                 │
└──────────────────────────────────────────────────────┘
┌─ FACE DETECTOR MARGIN ────────────────────────────────┐
│ [Slider: 0.0 ●─────────────────── | ] 1.0            │
│           0.0                      ↑  Input: 0        │
└──────────────────────────────────────────────────────┘
┌─ FACE DETECTOR ANGLES ────────────────────────────────┐
│ [Buttons: ✓ 0  │  90  │  180  │  270  ]              │
│           [RED]  [DARK]  [DARK]  [DARK]               │
└──────────────────────────────────────────────────────┘
┌─ FACE DETECTOR SCORE ─────────────────────────────────┐
│ [Slider: 0.5 ───────●───────────── | ] 1.0           │
│           0.0          ↑               Input: 0.5     │
└──────────────────────────────────────────────────────┘
```

#### FACE LANDMARKER Settings:
```
┌─ FACE LANDMARKER MODEL ───────────────────────────────┐
│ [Dropdown: 2dfan4 ▼]                                  │
└──────────────────────────────────────────────────────┘
┌─ FACE LANDMARKER SCORE ───────────────────────────────┐
│ [Slider: 0.5 ───────●───────────── | ] 1.0           │
│           0.0          ↑               Input: 0.5     │
└──────────────────────────────────────────────────────┘
```

#### FACE MASKING Settings:
```
┌─ FACE MASK TYPES ───────────────────────────────────┐
│ [Buttons: ✓ box  │  occlusion  │  area  │  region ]  │
│           [RED]     [DARK]        [DARK]   [DARK]     │
└──────────────────────────────────────────────────────┘
┌─ FACE MASK BLUR ───────────────────────────────────┐
│ [Slider: 0.3 ──●─────────────── | ] 1.0            │
│           0.0    ↑              Input: 0.3          │
└──────────────────────────────────────────────────────┘
┌─ FACE MASK PADDING ───────────────────────────────┐
│ Top:    [Slider: 0 ●────────── | ] [Input: 0]  ⟲  │
│ Right:  [Slider: 0 ●────────── | ] [Input: 0]  ⟲  │
│ Bottom: [Slider: 0 ●────────── | ] [Input: 0]  ⟲  │
│ Left:   [Slider: 0 ●────────── | ] [Input: 0]  ⟲  │
└──────────────────────────────────────────────────────┘
```

---

### 3️⃣ GLOBAL SETTINGS SECTION

**Type**: Collapsible accordion sections  
**Location**: Left panel, bottom  
**Always visible**: Execution Providers, Output Settings

#### EXECUTION PROVIDERS
```
┌─ EXECUTION PROVIDERS ──────────────────────────────────┐
│ [Buttons: ✓ cuda  │  tensorrt  │  cpu  ]              │
│           [RED]      [DARK]        [DARK]              │
│  └─ Auto-detect on load, show available only          │
└──────────────────────────────────────────────────────┘
┌─ EXECUTION THREAD COUNT ──────────────────────────────┐
│ [Slider: 8 ─────────────●─── | ] 16                   │
│           1              ↑    Input: 8  [⟲ Reset]    │
└──────────────────────────────────────────────────────┘
┌─ LOG LEVEL ───────────────────────────────────────────┐
│ [Dropdown: info ▼]                                    │
│  └─ Options: debug, info, warning, error              │
└──────────────────────────────────────────────────────┘
```

#### OUTPUT SETTINGS
```
┌─ OUTPUT IMAGE QUALITY ────────────────────────────────┐
│ [Slider: 80 ────────────●────── | ] 100              │
│            0             ↑       Input: 80            │
└──────────────────────────────────────────────────────┘
┌─ OUTPUT IMAGE SCALE ──────────────────────────────────┐
│ [Slider: 1.0 ●────────────────── | ] 4.0             │
│            0.5                    ↑  Input: 1.0      │
└──────────────────────────────────────────────────────┘
┌─ VIDEO MEMORY STRATEGY ───────────────────────────────┐
│ [Dropdown: strict ▼]                                  │
│  └─ Options: strict, moderate, aggressive             │
└──────────────────────────────────────────────────────┘
┌─ SKIP CONTENT ANALYSIS ───────────────────────────────┐
│ [Checkbox: ☐ ] Skip NSFW/violence checks              │
│  └─ Unchecked by default                              │
└──────────────────────────────────────────────────────┘
```

#### DOWNLOAD PROVIDERS
```
┌─ DOWNLOAD PROVIDERS ──────────────────────────────────┐
│ [Buttons: ✓ github  │  ✓ huggingface  ]               │
│           [RED]          [RED] (both enabled)         │
│  └─ Shows download source priority                    │
└──────────────────────────────────────────────────────┘
```

---

### 4️⃣ CENTER PANEL — MEDIA PICKER & I/O

**Type**: Drag-drop zones + file picker buttons  
**Location**: Center column  
**Sections**: Source, Target, Output Path

```
┌─────────────────────────────────────────────────────────┐
│  ▲ SOURCE                                           [×] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    🎬 Drag video/image here or [BROWSE]               │
│    Accepted: mp4, mov, jpg, png, webp                 │
│                                                         │
│  Current: ~/videos/source_video.mp4 (523 MB)          │
├─────────────────────────────────────────────────────────┤
│  [Clear] [Preview]                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  ▼ TARGET                                           [×] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    👤 Drag reference image here or [BROWSE]            │
│    Accepted: jpg, png, webp                            │
│                                                         │
│  Current: ~/faces/target_face.png (5.2 MB)            │
├─────────────────────────────────────────────────────────┤
│  [Clear] [Preview]                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  OUTPUT PATH                                            │
├─────────────────────────────────────────────────────────┤
│  [/mnt/c/Users/user/Documents/swap_____________________]│
│  [Browse Folder] [Clear]                               │
│  └─ Must be writable directory                         │
└─────────────────────────────────────────────────────────┘
```

**Drag-Drop Behavior**:
- **Hover**: Background #3a3a3a, border #ff4444 (3px solid)
- **Drop valid**: File loads, displays filename + size
- **Drop invalid**: Red error message "Invalid file type"
- **Transition**: 150ms
- **Z-index**: Ensure overlay doesn't cover right panel or settings

---

### 5️⃣ RIGHT PANEL — PREVIEW & FACE SELECTOR

**Location**: Right column, split into 2 sections  
**Width**: Responsive, min 300px

#### PREVIEW SECTION (Top 50%)
```
┌─────────────────────────────────────────────────────────┐
│ PREVIEW                                    [⊡] [⋮] [×] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│          ┌─────────────────────────────────┐           │
│          │      [Preview Image/Video]      │           │
│          │    (Responsive, fit container)  │           │
│          └─────────────────────────────────┘           │
│                                                         │
│  Preview Mode: [default ▼]                             │
│  Resolution:   [1024x1024 ▼]                           │
└─────────────────────────────────────────────────────────┘
```

#### FACE SELECTOR SECTION (Bottom 50%)
```
┌─────────────────────────────────────────────────────────┐
│ FACE SELECTOR                                       [×] │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Thumbnail] [Thumbnail] [Thumbnail]                   │
│  Face 0      Face 1      Face 2 (selected)             │
│  ┌──────┐   ┌──────┐    ┌──────────────┐              │
│  │      │   │      │    │ ┌──────────┐ │              │
│  │ [🔍] │   │ [🔍] │    │ │Reference│ │ [RED BORDER] │
│  │      │   │      │    │ │  face    │ │              │
│  └──────┘   └──────┘    │ └──────────┘ │              │
│                          └──────────────┘              │
│                                                         │
│  Selector Mode: [reference ▼]                          │
│  Order:         [large-small ▼]                        │
│  Gender:        [none ▼]                               │
│  Age Range:     [Slider: 0──●────────── | ] 100        │
│  Distance:      [Slider: 0.3────●────── | ] 1.0        │
│  Tracker Score: [Slider: 0.5────●────── | ] 1.0        │
│                                                         │
│  Face Models:                                           │
│  Occluder:      [x264_1 ▼]                             │
│  Pager:         [bisenet_resnet_34 ▼]                 │
│                                                         │
│  ┌─ FACE MASK TYPES ──────────────────────────────────┐│
│  │ [✓ box] [occlusion] [area] [region]                ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  FACE MASK BLUR: [Slider: 0.3 ──●──────── | ]         │
└─────────────────────────────────────────────────────────┘
```

**Behavior**:
- **Face thumbnails**: Click to select, white border on selected thumbnail
- **Age range slider**: Interactive, updates face detection in real-time preview
- **Dropdowns**: Click shows dropdown arrow rotation (90° → 270°), list appears below
- **Dropdown list**: Scrollable if >5 items, max-height 200px, never overlaps bottom panel
- **Transition**: All dropdown opens should smoothly slide down 200ms

---

### 6️⃣ DROPDOWN COMPONENT (Universal Pattern)

**All dropdowns follow this design**:

```
┌────────────────────────────────────────────┐
│  Model: [hyperswap_1a_256           ▼]     │
└────────────────────────────────────────────┘
                     ↓ (on click)
┌────────────────────────────────────────────┐
│  Model: [hyperswap_1a_256           ▲]     │
├────────────────────────────────────────────┤
│  hyperswap_1a_256 ✓                        │
│  hyperswap_1b_512                          │
│  ghost_640 (downloading...)                │
│  (scroll if needed)                        │
└────────────────────────────────────────────┘
```

**Visual Design**:
- **Closed**: Dark background #2a2a2a, border #444444, arrow right (▼)
- **Open**: Arrow rotates to (▲), list appears in modal-like container
- **Selected item**: Checkmark on right, text white
- **Hover item**: Background #3a3a3a
- **Downloading**: Text #ffaa00 (warning), italic
- **Unavailable**: Text #999999 (disabled)
- **Click outside**: Closes immediately, no animation
- **Keyboard**: Arrow keys navigate, Enter selects, Esc closes
- **Z-index**: Ensure list appears above all other content
- **Width**: Match parent input width
- **Max height**: 200px with scrollbar

---

### 7️⃣ SLIDER COMPONENT (Universal Pattern)

**All sliders follow this design**:

```
Min Value: 0.0                                Max Value: 1.0
│                                                        │
0 ────────────────●────────────────────────────────── 1.0
                   ↑
             Current: 0.5  [Input Field]  [⟲ Reset]

Behavior:
- Drag thumb: Smooth tracking, real-time value update
- Click track: Jump to position
- Input field: Type value, Enter applies
- Range: Enforce min/max boundaries
- Display: Show value in real-time near thumb
- Reset button: Restores to processor default value
```

**Visual Design**:
- **Track (inactive)**: #444444
- **Track (active)**: #ff4444
- **Thumb**: Circular, white, radius 8px, shadow 0 2px 8px rgba(0,0,0,0.5)
- **Hover thumb**: Scale 1.2, cursor grab
- **Dragging**: Scale 1.3, cursor grabbing
- **Input field**: Dark background #2a2a2a, border on focus #ff4444
- **Transition**: 100ms cubic-bezier(0.34, 1.56, 0.64, 1) (bouncy easing)

---

### 8️⃣ BUTTONS & TOGGLES (Universal Pattern)

#### Radio Toggle Buttons (Multi-option, single select)
```
[✓ option1] [option2] [option3] [option4]
[  RED   ]  [ DARK  ] [ DARK  ] [ DARK  ]
```

**Design**:
- **Unselected**: Background #2a2a2a, border 1px #444444, text #fff
- **Selected**: Background #ff4444, border 0, text #fff, checkmark icon
- **Hover unselected**: Background #3a3a3a
- **Hover selected**: Background #ff5555
- **Active state**: Scale 0.98 (press effect)
- **Transition**: 150ms

#### Checkbox
```
[☐] Option Label
[☑] Option Label (checked)
```

**Design**:
- **Unchecked**: Border 2px #444444, background transparent
- **Checked**: Background #ff4444, checkmark white
- **Hover**: Border #ff4444
- **Disabled**: Opacity 0.5
- **Transition**: 100ms

---

### 9️⃣ TERMINAL / LOG OUTPUT SECTION

**Location**: Right panel, bottom (or floating modal)  
**Type**: Scrollable code block, read-only  
**Max height**: 300px (scrollable)

```
┌─────────────────────────────────────────────────────────┐
│ TERMINAL                                    [⊕] [×] [⋮] │
├─────────────────────────────────────────────────────────┤
│ [FACEFUSION_CORE] Initializing CUDA...                  │
│ [FACEFUSION_CORE] Loading models from .assets/...      │
│ [FACEFUSION_CORE] Available: face_swapper,              │
│ [FACEFUSION_CORE] Processing step 1 of 1                │
│ [FACEFUSION_CORE] Choose an image for the source!      │
│                                                         │
│  (scrollable, fixed-width mono font)                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Behavior**:
- **Auto-scroll**: New messages appear at bottom, auto-scroll if already scrolled to bottom
- **Color coding**:
  - `[FACEFUSION_CORE]` → #4488ff (info blue)
  - Errors (contain "Error") → #ff4444 (red)
  - Warnings (contain "WARNING") → #ffaa00 (orange)
  - Success (contain "success", "Complete") → #44aa44 (green)
- **Copy button**: Select text + Ctrl+C works
- **Clear button**: Clears all logs (with confirmation)
- **Transition**: Messages fade in 200ms

---

### 🔟 ACTION BUTTONS

#### START / RUN BUTTON
```
┌──────────────────────────────────┐
│      ▶ START (Processing)        │
│    [RED #ff4444, white text]     │
│    Height: 48px, width: full     │
│    Disabled when: no media input │
└──────────────────────────────────┘
```

**States**:
- **Ready**: Background #ff4444, cursor pointer
- **Hover**: Background #ff5555, scale 1.02
- **Active**: Scale 0.98
- **Processing**: Text "Processing..." + spinner, disable click, opacity 0.8
- **Complete**: Text "Complete ✓", background #44aa44 for 2 seconds, then reset

#### SECONDARY BUTTONS (Clear, Reset, Browse)
```
[CLEAR] [BROWSE] [RESET]
[DARK]  [DARK]   [DARK]
```

**Design**:
- Background: #2a2a2a
- Border: 1px #444444
- Hover: Background #3a3a3a
- Click: Scale 0.95
- Height: 36px

---

## ⚙️ RESPONSIVE BEHAVIOR

### Desktop (>1200px)
- 3-column layout as shown (40-30-30)
- Full preview in right panel
- Hover states fully functional

### Tablet (768px - 1200px)
- 2-column layout: Left (50%) + Right (50%)
- Settings scrollable vertically
- Preview stacked below media picker

### Mobile (<768px)
- Single column, full-width sections stacked
- Accordion-style (collapsible sections)
- Dropdowns trigger full-screen modal
- Sliders use larger touch targets (48px height)

---

## 🎯 INTERACTION PATTERNS & UX DECISIONS

### Processor Selection (Radio Buttons)
**Decision**: Why radio buttons, not tabs?
- Radio buttons support grid layout (more processors visible)
- Takes less vertical space
- Easier to scan 2-column grid
- Clear visual hierarchy (red = active)

**Behavior**:
- Click processor → Immediately show processor-specific settings panel (150ms fade-in)
- Hide unrelated settings panels (fade-out)
- Preserve user's custom values when switching back to same processor
- Always show "Global Settings" section (Execution, Output, etc.)

### Dropdowns (Model Selection)
**Decision**: Why not autocomplete search?
- Most users have 1-3 models installed
- Simpler UX, fewer edge cases
- Show download status inline (user knows what's available)

**Behavior**:
- Click dropdown → Arrow rotates, list slides down
- Item hover → Background highlight
- Click item → Dropdown closes, field updates instantly
- Arrow key navigation → Up/Down moves selection, Enter picks
- Escape key → Closes dropdown, preserves last selected value
- If list has >5 items → Add scrollbar, max-height 200px
- Selected item shows checkmark

### Sliders (Numeric Values)
**Decision**: Why combine slider + input field?
- Slider for quick adjustments (intuitive)
- Input for precise values (accessibility)
- Link icon (batch processing) appears on hover

**Behavior**:
- Drag thumb → Real-time update, show tooltip with current value
- Click track → Jump to position
- Type in input → Apply on Enter or blur
- Reset button (⟲) → Restores processor default
- Enforce min/max boundaries (prevent invalid values)
- Debounce input changes (300ms) before re-rendering preview

### Drag-Drop Zone (Media Input)
**Decision**: Why drag-drop + file picker?
- Users expect both
- Drag-drop is faster for power users
- File picker ensures accessibility
- Shows file info (size, type) after drop

**Behavior**:
- Hover with file → Border #ff4444, background #3a3a3a (clear drop zone)
- Drop valid file → Show filename + size, enable Preview button
- Drop invalid → Red error message, fade out after 4 seconds
- Click [BROWSE] → Native OS file picker
- Click [CLEAR] → Remove file, reset UI
- Click [PREVIEW] → Open preview in lightbox/modal (image) or media player (video)

### Face Selector Grid (Thumbnails)
**Decision**: Why grid, not single selection?
- Shows all detected faces at once
- User can visually identify target face
- Reduces clicks vs. carousel

**Behavior**:
- Display faces as 3 columns of clickable thumbnails
- Selected face has white 3px border + red highlight
- Hover unselected → Border #ff4444
- Click → Select, update main preview on right
- Age/Gender/Distance sliders → Filter faces in real-time
- If no faces detected → Show "No faces detected. Adjust detection settings."

### Terminal / Log Output
**Decision**: Why show logs inline vs. separate tab?
- Users need to see what's happening during processing
- Inline keeps focus on output
- Users can scroll up to see earlier messages

**Behavior**:
- New messages append to bottom
- Auto-scroll only if user was at bottom (preserve scroll position if reading history)
- Color-code by severity (error red, warning orange, info blue)
- Max 500 lines in memory (circular buffer)
- [CLEAR] button removes all logs with confirmation

### Progress During Processing
**Decision**: How to show progress?
- Use progress bar + percentage + ETA
- Also show current step (e.g., "Step 3 of 12")
- Allow cancellation

**Visual**:
```
Processing: Step 3 of 12 (frame enhancement)
┌─────────────────────────────────────────────┐
│ ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ 25%
└─────────────────────────────────────────────┘
Estimated time remaining: 4m 32s
[CANCEL]
```

---

## 🛡️ VALIDATION & ERROR HANDLING

### Input Validation
- **No source file**: START button disabled, message "Select source media"
- **No target file**: START button disabled (for processors that need it), message "Select target"
- **Invalid output path**: Error message, suggest creating directory
- **Model not downloaded**: Warning badge on dropdown, "Download missing models?" button
- **GPU not available**: Warning message, suggest CPU mode

### Error Messages
- **Format**: Red (#ff4444) banner at top of section
- **Duration**: Persist until user dismisses or fixes issue
- **Example**: "GPU error: CUDA out of memory. Reduce output scale or use CPU mode."

### Confirmation Dialogs
- **Clear all data**: "Are you sure? This cannot be undone."
- **Cancel processing**: "Stop current job? Progress will be lost."

---

## ♿ ACCESSIBILITY

### Keyboard Navigation
- Tab through all inputs
- Shift+Tab to reverse
- Enter to activate buttons/submit
- Space to toggle checkboxes
- Arrow keys in sliders and dropdowns
- Escape to close modals/dropdowns

### Screen Readers
- All buttons have aria-labels
- Form inputs have associated labels
- Error messages associated with inputs (aria-describedby)
- Live region for status updates (aria-live="polite")

### Visual Accessibility
- Color contrast: WCAG AA minimum (4.5:1 for text)
- Focus indicators: Visible 2px outline, color #ff4444
- Don't rely on color alone (use text labels + icons)
- Reduced motion: Respect prefers-reduced-motion, disable animations

---

## 🎬 ANIMATION & TRANSITIONS

### Timing
- **Micro-interactions** (button click, toggle): 100-150ms
- **State changes** (dropdown open, panel switch): 200ms
- **Page transitions**: 300ms
- **Loading states**: Spinner 1s rotation loop

### Easing
- **Standard**: cubic-bezier(0.4, 0, 0.2, 1) (Material Design)
- **Entrance**: cubic-bezier(0.34, 1.56, 0.64, 1) (slight bounce)
- **Exit**: cubic-bezier(0.4, 0, 1, 1) (ease-out)

### What Animates
- ✓ Button hover/press
- ✓ Dropdown open/close
- ✓ Slider drag
- ✓ Panel fade-in/out (processor settings)
- ✓ Progress bar fill
- ✓ Error messages (fade-in/out)
- ✗ Dropdowns opening (use CSS transform: translateY)
- ✗ Spam animations (keep professional)

---

## 🔌 INTEGRATION CHECKLIST

Before deploying, ensure:

- [ ] All processor radio buttons update settings dynamically
- [ ] Dropdown arrow rotates on open/close
- [ ] Sliders show real-time value near thumb
- [ ] Input fields validate on blur + Enter
- [ ] Drag-drop zones show visual feedback on hover
- [ ] Media preview opens in modal (not inline)
- [ ] Face selector grid filters in real-time
- [ ] Progress bar shows accurate step count
- [ ] Terminal auto-scrolls on new messages
- [ ] All buttons are accessible (keyboard + screen reader)
- [ ] Responsive layout works on 320px - 4K screens
- [ ] Color contrast passes WCAG AA
- [ ] No UI overlaps (dropdowns, modals, etc.)
- [ ] Settings persist when switching processors
- [ ] Error messages are dismissible
- [ ] GPU/CPU selection is visible and functional

---

## 📝 CODE IMPLEMENTATION NOTES

### Gradio-Specific Guidance
```python
# Use gr.Blocks() for full control
# Use gr.Group() for sectioning (with visible=False for conditional display)
# Use gr.Column() for 3-column layout
# Use gr.Dropdown() with allow_custom_value=False
# Use gr.Slider() with step parameter
# Use gr.Textbox() for inputs (interactive=True)
# Use gr.Radio() for exclusive selection
# Use gr.Checkbox() for boolean options
# Use gr.HTML() for custom styling (CSS in <style> tag)
# Use gr.Button() with size="lg" for primary action
```

### CSS Overrides
```css
/* Root styling */
:root {
  --bg-primary: #1a1a1a;
  --bg-secondary: #2a2a2a;
  --bg-tertiary: #3a3a3a;
  --accent: #ff4444;
  --text-primary: #ffffff;
  --border: #444444;
}

/* Gradio component customization */
.gradio-dropdown {
  /* Custom dropdown styling */
}

.gradio-slider {
  /* Custom slider styling */
}
```

---

## 🎨 COLOR REFERENCE (Hex Codes)

```
#1a1a1a - Primary background
#2a2a2a - Secondary background / input background
#3a3a3a - Hover state / active background
#444444 - Borders / dividers
#ffffff - Primary text / icons
#cccccc - Secondary text
#999999 - Disabled text / hints
#ff4444 - Accent / selected / active
#ff5555 - Accent hover
#ffaa00 - Warning / attention
#44aa44 - Success / completion
#4488ff - Info / messages
```

---

**Document Version**: 1.0  
**Last Updated**: 2026-07-08  
**Status**: Ready for Implementation