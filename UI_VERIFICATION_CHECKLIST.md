# NTHX Fusion UI — Verification & Quality Assurance Checklist

**Use this after implementation to verify all components are pixel-perfect and functional.**

---

## ✅ LAYOUT & STRUCTURE

- [ ] Header displays "NTHX Fusion 0.1.0" (not "FaceFusion 3.7.1")
- [ ] 3-column layout visible on desktop (40-30-30 width split)
- [ ] Left panel shows processor selector + settings
- [ ] Center panel shows media picker (Source, Target, Output Path)
- [ ] Right panel shows preview + face selector
- [ ] All panels properly spaced (16px padding, 12px gaps)
- [ ] Responsive on tablet (2 columns) and mobile (1 column, stacked)

---

## 🎨 COLORS & STYLING

- [ ] Background is #1a1a1a (dark, not pure black)
- [ ] Secondary backgrounds are #2a2a2a (input boxes, cards)
- [ ] Hover states show #3a3a3a
- [ ] Borders are #444444 (not bright white)
- [ ] Text is #ffffff (white)
- [ ] All selected/active states use #ff4444 (red)
- [ ] No bright gradients (professional, not AI-generated)
- [ ] Border radius is 4px (sharp, not rounded)
- [ ] All text has sufficient contrast (WCAG AA pass)

---

## 🎛️ PROCESSOR SELECTOR (Radio Buttons)

- [ ] Displays as 2-column grid
- [ ] All processors visible: face_swapper, face_enhancer, frame_enhancer, face_detection, face_selection, masking, etc.
- [ ] Unselected button: dark background #2a2a2a, border #444444
- [ ] Selected button: red background #ff4444, white checkmark icon
- [ ] Clicking processor updates settings panel below (fade-in/out 150ms)
- [ ] Default processor is "face_swapper" selected on load
- [ ] Hover unselected shows #3a3a3a
- [ ] Hover selected shows #ff5555

**Test**: Click each processor → verify correct settings panel appears

---

## 📊 FACE SWAPPER SETTINGS

- [ ] Model dropdown shows "hyperswap_1a_256" (or installed model)
  - [ ] Arrow points down (▼) when closed, up (▲) when open
  - [ ] Click opens scrollable list (don't cover below content)
  - [ ] List shows all available models + download status
  - [ ] Click item → dropdown closes, field updates
- [ ] Pixel Boost dropdown (256x256, 512x512, etc.)
- [ ] Weight slider:
  - [ ] Range 0.0 to 1.0
  - [ ] Shows current value (e.g., 0.5)
  - [ ] Input field allows typing
  - [ ] Reset button (⟲) restores default
  - [ ] Dragging updates real-time
- [ ] All fields functional, no errors on change

---

## 📊 FACE ENHANCER SETTINGS

- [ ] Model dropdown (gfpgan_1.4, etc.)
- [ ] Weight slider (0.0 to 1.0)
  - [ ] Value displays near thumb
  - [ ] Input field present
  - [ ] Reset button works

---

## 📊 FRAME ENHANCER SETTINGS

- [ ] Model dropdown (realesrgan_x2plus, etc.)

---

## 📊 FACE DETECTION SETTINGS

- [ ] Model dropdown (yolo_face, etc.)
- [ ] Size dropdown (640x640, 416x416, etc.)
- [ ] Margin slider (0.0 to 1.0)
- [ ] Angles buttons: [✓ 0] [90] [180] [270]
  - [ ] Selected angle has red background
  - [ ] Multiple angles can be selected (toggle behavior)
  - [ ] Visual feedback on click
- [ ] Score slider (0.0 to 1.0)
  - [ ] Value field + input
  - [ ] Reset button
- [ ] Landmarker model dropdown (2dfan4, etc.)
- [ ] Landmarker score slider (0.0 to 1.0)

---

## 📊 FACE SELECTION SETTINGS

- [ ] Selector mode dropdown (reference, largest, smallest, etc.)
- [ ] Order dropdown (large-small, etc.)
- [ ] Gender dropdown (none, male, female, etc.)
- [ ] Age range slider (0 to 100)
  - [ ] Real-time filtering of face grid
- [ ] Distance slider (0.3 to 1.0)
- [ ] Tracker score slider (0.5 to 1.0)
- [ ] Face Occluder model dropdown (x264_1, etc.)
- [ ] Face Pager model dropdown (bisenet_resnet_34, etc.)

---

## 📊 FACE MASKING SETTINGS

- [ ] Mask type buttons: [✓ box] [occlusion] [area] [region]
  - [ ] Selected has red background + checkmark
  - [ ] Click toggles (multiple can be selected)
- [ ] Blur slider (0.0 to 1.0)
  - [ ] Value displays
  - [ ] Input field works
  - [ ] Reset button present
- [ ] Padding controls (Top, Right, Bottom, Left)
  - [ ] Each has slider + input field
  - [ ] Each has reset button (⟲)
  - [ ] All functional

---

## 🔧 GLOBAL SETTINGS

### Execution Providers
- [ ] Shows buttons: [✓ cuda] [tensorrt] [cpu]
- [ ] Selected has red background
- [ ] Only shows available providers (auto-detect GPU)
- [ ] Clicking provider updates immediately
- [ ] Visual feedback on selection

### Execution Thread Count
- [ ] Slider range 1 to 16 (or max available cores)
- [ ] Default value ~8
- [ ] Input field for typing
- [ ] Reset button

### Log Level
- [ ] Dropdown shows: debug, info, warning, error
- [ ] Default "info"
- [ ] Changes apply immediately

### Output Quality
- [ ] Slider 0 to 100
- [ ] Default 80
- [ ] Input field works

### Output Scale
- [ ] Slider 0.5 to 4.0
- [ ] Default 1.0
- [ ] Input field for precise values

### Video Memory Strategy
- [ ] Dropdown: strict, moderate, aggressive
- [ ] Default "strict"

### Skip Content Analysis
- [ ] Checkbox, unchecked by default
- [ ] Can be toggled

### Download Providers
- [ ] Buttons: [✓ github] [✓ huggingface]
- [ ] Both enabled by default (red background)
- [ ] Toggle on/off
- [ ] Visual feedback

---

## 📤 MEDIA PICKER (Center Panel)

### Source Media
- [ ] Drag-drop zone visible with instructions
- [ ] Accepted formats shown (mp4, mov, jpg, png, webp)
- [ ] Drag file → zone highlights red border (#ff4444)
- [ ] Drop file → shows filename + size (e.g., "source_video.mp4 (523 MB)")
- [ ] [BROWSE] button opens file picker
- [ ] [CLEAR] button removes file
- [ ] [PREVIEW] button opens lightbox with video/image
- [ ] Drop wrong file type → red error message (fades after 4 seconds)

### Target Media
- [ ] Same as Source but for reference face
- [ ] Shows thumbnail preview if image

### Output Path
- [ ] Text input for output directory
- [ ] [Browse Folder] button opens directory picker
- [ ] Shows current path
- [ ] Validation: warns if directory not writable
- [ ] [CLEAR] button resets to default

---

## 👁️ PREVIEW PANEL (Right Panel, Top)

- [ ] Shows "PREVIEW" header with [⊡] [⋮] [×] buttons
- [ ] Displays preview image/video (responsive, fits container)
- [ ] Preview Mode dropdown (default, etc.)
- [ ] Resolution dropdown (1024x1024, etc.)
- [ ] Image/video scales properly without distortion
- [ ] Click [×] closes preview

---

## 👤 FACE SELECTOR PANEL (Right Panel, Bottom)

- [ ] Shows grid of detected face thumbnails
- [ ] Each face is clickable thumbnail
- [ ] Selected face has white border (3px) + red highlight
- [ ] Hover shows #ff4444 border on unselected faces
- [ ] Selector Mode dropdown (reference, etc.)
- [ ] Order dropdown (large-small, etc.)
- [ ] Gender dropdown (none, male, female)
- [ ] Age Range slider:
  - [ ] Ranges 0 to 100
  - [ ] Real-time filters visible faces
- [ ] Face Distance slider (0.3 to 1.0)
- [ ] Face Tracker Score slider (0.5 to 1.0)
- [ ] Face Occluder dropdown (x264_1, etc.)
- [ ] Face Pager dropdown (bisenet_resnet_34, etc.)
- [ ] Face Mask Types buttons work
- [ ] Face Mask Blur slider functional

**Test**: Move age slider → face grid updates in real-time

---

## 📟 TERMINAL / LOG OUTPUT

- [ ] Shows scrollable log area (max 300px height or less)
- [ ] Messages appear with [FACEFUSION_CORE] prefix
- [ ] Error messages in red (#ff4444)
- [ ] Warnings in orange (#ffaa00)
- [ ] Info in blue (#4488ff)
- [ ] New messages fade in (200ms)
- [ ] Auto-scrolls only if already at bottom
- [ ] Manual scroll preserved (doesn't jump)
- [ ] [CLEAR] button removes all logs (shows confirmation)
- [ ] Copy text works (Ctrl+C, Select+Copy)
- [ ] Max 500 lines in memory (older messages removed)

---

## ▶️ PROCESSING & PROGRESS

- [ ] START button is prominent (red #ff4444, large)
- [ ] START disabled if no source media
- [ ] During processing:
  - [ ] Text changes to "Processing..." + spinner
  - [ ] Button disables (opacity 0.8)
  - [ ] Progress bar shows step (e.g., "3 of 12")
  - [ ] Percentage fills from 0% to 100%
  - [ ] ETA displayed ("4m 32s remaining")
  - [ ] [CANCEL] button appears
- [ ] On completion:
  - [ ] Progress shows 100%
  - [ ] Button text changes to "Complete ✓"
  - [ ] Background turns green (#44aa44) for 2 seconds
  - [ ] Resets to "START" after
  - [ ] Output file location shown

- [ ] [CLEAR] button resets all fields

---

## 🎮 DROPDOWN BEHAVIOR (All Dropdowns)

- [ ] Closed state: arrow points down (▼)
- [ ] Click → arrow rotates up (▲), list slides down 200ms
- [ ] List shows all items
- [ ] List max-height 200px with scrollbar if >5 items
- [ ] Selected item shows checkmark (✓)
- [ ] Hover item → background #3a3a3a
- [ ] Click item → closes dropdown, updates field
- [ ] Click outside → closes dropdown (no animation)
- [ ] Keyboard: Arrow keys navigate, Enter selects, Esc closes
- [ ] List never covers content below (scrolls page if needed)
- [ ] Downloading models show with yellow (#ffaa00) text + italic

---

## 🎛️ SLIDER BEHAVIOR (All Sliders)

- [ ] Slider visible with track + thumb
- [ ] Track: inactive #444444, active #ff4444
- [ ] Thumb: white, radius 8px, shadow
- [ ] Hover thumb: scale 1.2, cursor grab
- [ ] Drag thumb: real-time value update, scale 1.3, cursor grabbing
- [ ] Value shows near thumb (e.g., "0.5")
- [ ] Input field below slider:
  - [ ] Can type value
  - [ ] Enter applies change
  - [ ] Blur also applies
  - [ ] Validates min/max boundaries
- [ ] Reset button (⟲) beside input:
  - [ ] Hover shows tooltip "Reset to default"
  - [ ] Click restores processor default value
- [ ] Smooth easing (cubic-bezier spring animation, 100ms)
- [ ] Prevent invalid values (enforce min/max)

---

## ☑️ CHECKBOX BEHAVIOR

- [ ] Unchecked: border 2px #444444, transparent background
- [ ] Checked: background #ff4444, white checkmark
- [ ] Hover: border #ff4444
- [ ] Click toggles state
- [ ] Label clickable (click label toggles checkbox)
- [ ] Keyboard: Space toggles

---

## 🖱️ DRAG-DROP BEHAVIOR

- [ ] Normal state: light border #444444, instructions visible
- [ ] Hover with file: border 3px #ff4444, background #3a3a3a
- [ ] Drop valid file:
  - [ ] Border returns to normal
  - [ ] Filename + size displayed below zone
  - [ ] [PREVIEW] button enabled
  - [ ] [CLEAR] button available
- [ ] Drop invalid file:
  - [ ] Red error message appears (e.g., "Invalid file type")
  - [ ] Message fades after 4 seconds
  - [ ] Drop zone resets

---

## ⌨️ KEYBOARD NAVIGATION

- [ ] Tab cycles through all inputs
- [ ] Shift+Tab reverses
- [ ] Focus indicators visible (2px outline #ff4444)
- [ ] Enter activates buttons
- [ ] Space toggles checkboxes + radio buttons
- [ ] Arrow keys in sliders (left/right adjust value)
- [ ] Arrow keys in dropdowns (up/down navigate items)
- [ ] Escape closes dropdowns + modals
- [ ] No focus traps

---

## ♿ ACCESSIBILITY

- [ ] All buttons have aria-labels
- [ ] All inputs have associated labels
- [ ] Error messages linked with aria-describedby
- [ ] Live regions for status updates (aria-live="polite")
- [ ] Color not only indicator (text labels present)
- [ ] Reduced motion respected:
  - [ ] Check browser preferences
  - [ ] Disable animations if prefers-reduced-motion set
- [ ] Contrast ratio ≥ 4.5:1 for all text
- [ ] Touch targets ≥ 44px on mobile

---

## 📱 RESPONSIVE DESIGN

### Desktop (>1200px)
- [ ] 3-column layout (40-30-30)
- [ ] All sections visible
- [ ] Hover states work

### Tablet (768px - 1200px)
- [ ] 2-column layout: Left (50%) + Right (50%)
- [ ] Settings scrollable
- [ ] Preview stacked below

### Mobile (<768px)
- [ ] Single column, full-width stacked sections
- [ ] Accordion sections collapsible
- [ ] Dropdowns trigger full-screen modal (not inline)
- [ ] Sliders have larger touch targets (48px)
- [ ] Touch-friendly spacing
- [ ] No horizontal scroll

---

## ❌ ERROR HANDLING

- [ ] No source media → "Select source media" message, START disabled
- [ ] No target media (if required) → "Select target" message
- [ ] Invalid output path → "Output directory not writable. Create?"
- [ ] Model not downloaded → Yellow warning badge, "Download?" option
- [ ] GPU not available → "CUDA unavailable. Switch to CPU?" suggestion
- [ ] Processing error → Red error banner with details + [RETRY] button
- [ ] All errors dismissible (×) or auto-dismiss (4 seconds)

---

## 🎨 VISUAL POLISH

- [ ] No visible jank or layout shifts during interactions
- [ ] All transitions smooth (150-200ms)
- [ ] Loading spinners smooth rotation (1s loop)
- [ ] Icons consistent (checkmarks, arrows, etc.)
- [ ] Spacing consistent throughout
- [ ] Text sizes match spec (labels 12px, body 14px, headings 16px)
- [ ] No AI-generated look (no gradients, no overly round corners, sharp professional)
- [ ] Consistent button styling
- [ ] All form controls aligned properly

---

## 🔗 INTEGRATION

- [ ] CLI flags work: `--processors face_swapper` sets processor
- [ ] Execution providers match CLI: `--execution-providers cuda tensorrt cpu`
- [ ] Output path accepts user paths: `-o /custom/path`
- [ ] Source/target paths in CLI: `-s source.mp4 -t target.png`
- [ ] Model downloads triggered from UI: [Download] button
- [ ] Progress bar syncs with backend processing
- [ ] Logs stream in real-time
- [ ] Output files created in specified directory
- [ ] No console errors in browser developer tools

---

## 🧪 FINAL TESTS

Run these before declaring "done":

1. **Processor Switch Test**: Click each processor → verify correct settings appear, old settings hide
2. **Dropdown Test**: Click all dropdowns → arrow rotates, list appears, no overlap
3. **Slider Test**: Drag all sliders → real-time value updates, input field syncs
4. **File Drop Test**: Drag valid + invalid files → correct feedback
5. **Face Detection Test**: Load media → faces detected + grid shows thumbnails
6. **Processing Test**: Click START → progress bar runs, logs update, output created
7. **Mobile Test**: Resize to 375px → layout stacks, touch targets adequate
8. **Keyboard Test**: Tab through all controls → all inputs reachable
9. **Error Test**: Trigger error (no GPU) → error displays clearly, option to fix
10. **Performance Test**: Open DevTools → no layout thrashing, smooth 60fps animations

---

## 📋 SIGN-OFF

**Implementation Complete**: [ ]  
**All Checks Passed**: [ ]  
**Ready for Production**: [ ]  

Date: ________________  
Verified By: ________________  

---

**If any checkbox fails, note it below and create issue:**

```
FAILED CHECKS:
- [ ] (Component) (Issue description)
- [ ] (Component) (Issue description)
```