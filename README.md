# ⚡ Clean Hyprland Configuration

Uma configuração minimalista e organizada["software","Hyprland","Wayland compositor"] no Arch Linux.

Focada em:

* Performance
* Visual clean
* Workflow rápido
* Integração com Wayland
* Setup moderno
* Simplicidade

---

# 🐧 Stack

* Hyprland
* Waybar
* Kitty
* Dolphin
* Wlogout
* Swaylock
* Hyprshot
* PipeWire
* Swww
* Conky

---

# 🚀 Features

✔ Workspaces dinâmicos

✔ Blur e animações suaves

✔ Screenshot estilo Windows 11

✔ Controle multimídia

✔ Monitor lateral com Conky

✔ Wallpaper automático

✔ Power menu moderno

✔ Atalhos otimizados

✔ Configuração organizada

---

# 📦 Dependências

## Core

```bash
sudo pacman -S hyprland kitty dolphin waybar
```

## Screenshot

```bash
sudo pacman -S grim slurp wl-clipboard libnotify
```

```bash
yay -S hyprshot
```

## Wallpaper

```bash
sudo pacman -S swww
```

## Áudio

```bash
sudo pacman -S pipewire wireplumber pavucontrol
```

## Player Control

```bash
sudo pacman -S playerctl
```

## Lockscreen

```bash
sudo pacman -S swaylock
```

## Brightness

```bash
sudo pacman -S brightnessctl
```

## Monitor

```bash
sudo pacman -S conky btop
```

---

# 🖥️ Visual

## Gaps

```ini
general {
    gaps_in = 2
    gaps_out = 3
}
```

## Borders

```ini
border_size = 2
```

## Blur

```ini
blur {
    enabled = true
    size = 3
    passes = 1
}
```

## Rounded Corners

```ini
rounding = 2
```

---

# ✨ Animations

Configuração suave e rápida:

```ini
animation = windows, 1, 4.79, easeOutQuint
animation = fade, 1, 3.03, quick
animation = workspaces, 1, 1.94, almostLinear, fade
```

---

# ⌨️ Keybinds

## Terminal

```ini
SUPER + Q
```

## File Manager

```ini
SUPER + E
```

## Launcher

```ini
SUPER + R
```

## Firefox

```ini
SUPER + F
```

## Discord

```ini
SUPER + D
```

## Steam

```ini
CTRL + SHIFT + J
```

## Screenshot

```ini
CTRL + SHIFT + S
```

## Toggle Conky

```ini
CTRL + SHIFT + ESC
```

## Toggle Floating

```ini
SUPER + V
```

## Kill Window

```ini
SUPER + C
```

---

# 📸 Screenshot

Hyprshot || Wayland screenshot utility for Hyprland:

```ini
bind = CTRL SHIFT, S, exec, hyprshot -m region
```

---

# 🖼️ Wallpaper

Inicialização automática:

```ini
exec-once = swww init
exec-once = python3 ~/.config/hypr/scripts/wallpaper.py
```

---

# 📊 Conky

Monitor lateral minimalista:

```ini
bind = CTRL SHIFT, ESCAPE, exec, pkill conky || conky -c ~/.config/conky/conky.conf
```

---

# 🔊 Multimedia Keys

## Volume

```ini
AudioRaiseVolume
AudioLowerVolume
AudioMute
```

## Brightness

```ini
MonBrightnessUp
MonBrightnessDown
```

## Media

```ini
AudioNext
AudioPause
AudioPrev
```

---

# 🧠 Layout

## Dwindle

```ini
dwindle {
    pseudotile = true
    preserve_split = true
}
```

---

# 🪟 Window Rules

## Ignore maximize

```ini
suppress_event = maximize
```

## XWayland fixes

```ini
no_focus = true
```

---

# 🔄 Reload Config

```bash
hyprctl reload
```

---

# 🎨 Design Philosophy

Este setup foi feito para:

* manter o desktop limpo
* consumir poucos recursos
* ser rápido no dia a dia
* ter visual moderno
* integrar perfeitamente com Wayland

Inspirado em:

* Kali Linux
* Minimal setups
* Cyberpunk themes
* Rice Linux community

---

# 🐧 System

* Arch Linux
* Hyprland
* Wayland
* AMD Ryzen 7 1700

---

# 💀 Final

```txt
> Simple. Fast. Clean.
```
