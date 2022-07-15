<!DOCTYPE html>
<!-- saved from url=(0051)https://www.jdoodle.com/python3-programming-online/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style id="ace-gruvbox">.ace-gruvbox .ace_gutter-active-line {background-color: #3C3836;}.ace-gruvbox {color: #EBDAB4;background-color: #1D2021;}.ace-gruvbox .ace_invisible {color: #504945;}.ace-gruvbox .ace_marker-layer .ace_selection {background: rgba(179, 101, 57, 0.75)}.ace-gruvbox.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #002240;}.ace-gruvbox .ace_keyword {color: #8ec07c;}.ace-gruvbox .ace_comment {font-style: italic;color: #928375;}.ace-gruvbox .ace-statement {color: red;}.ace-gruvbox .ace_variable {color: #84A598;}.ace-gruvbox .ace_variable.ace_language {color: #D2879B;}.ace-gruvbox .ace_constant {color: #C2859A;}.ace-gruvbox .ace_constant.ace_language {color: #C2859A;}.ace-gruvbox .ace_constant.ace_numeric {color: #C2859A;}.ace-gruvbox .ace_string {color: #B8BA37;}.ace-gruvbox .ace_support {color: #F9BC41;}.ace-gruvbox .ace_support.ace_function {color: #F84B3C;}.ace-gruvbox .ace_storage {color: #8FBF7F;}.ace-gruvbox .ace_keyword.ace_operator {color: #EBDAB4;}.ace-gruvbox .ace_punctuation.ace_operator {color: yellow;}.ace-gruvbox .ace_marker-layer .ace_active-line {background: #3C3836;}.ace-gruvbox .ace_marker-layer .ace_selected-word {border-radius: 4px;border: 8px solid #3f475d;}.ace-gruvbox .ace_print-margin {width: 5px;background: #3C3836;}.ace-gruvbox .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNQUFD4z6Crq/sfAAuYAuYl+7lfAAAAAElFTkSuQmCC") right repeat-y;}
/*# sourceURL=ace/css/ace-gruvbox */</style><style id="autocompletion.css">.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #CAD6FA;    z-index: 1;}.ace_dark.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {    background-color: #3a674e;}.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid #abbffe;    margin-top: -1px;    background: rgba(233,233,253,0.4);    position: absolute;    z-index: 2;}.ace_dark.ace_editor.ace_autocomplete .ace_line-hover {    border: 1px solid rgba(109, 150, 13, 0.8);    background: rgba(58, 103, 78, 0.62);}.ace_completion-meta {    opacity: 0.5;    margin: 0.9em;}.ace_completion-message {    color: blue;}.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #2d69c7;}.ace_dark.ace_editor.ace_autocomplete .ace_completion-highlight{    color: #93ca12;}.ace_editor.ace_autocomplete {    width: 300px;    z-index: 200000;    border: 1px lightgray solid;    position: fixed;    box-shadow: 2px 3px 5px rgba(0,0,0,.2);    line-height: 1.4;    background: #fefefe;    color: #111;}.ace_dark.ace_editor.ace_autocomplete {    border: 1px #484747 solid;    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.51);    line-height: 1.4;    background: #25282c;    color: #c1c1c1;}
/*# sourceURL=ace/css/autocompletion.css */</style><style>.ace_snippet-marker {    -moz-box-sizing: border-box;    box-sizing: border-box;    background: rgba(194, 193, 208, 0.09);    border: 1px dotted rgba(211, 208, 235, 0.62);    position: absolute;}</style><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;padding: 0;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}
/*# sourceURL=ace/css/ace_editor.css */</style><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><meta property="og:url" content="https://www.jdoodle.com"><meta property="og:type" content="website"><meta property="og:title" content="JDoodle - free Online  Compiler, Editor for Java, C/C++, etc"><meta property="og:description" content="JDoodle is a free Online  Compiler, Editor, IDE  for Java, C, C++, PHP, Perl, Python, Ruby and many more.  you can run your programs on the fly online and you can save and share them with others. Quick and Easy way to compile and run programs online."><meta property="og:image" content="https://www.jdoodle.com/assets/jdoodle-fb.png"><meta property="og:image:alt" content="JDoodle"><meta name="google-site-verification" content="UvObv0WXViGO2pEP8egoe3k1sXqHcsSeAfEEjnUyuXg"><meta name="msvalidate.01" content="93539EB8D681BD90594A81FCAF6560BC"><style type="text/css">svg:not(:root).svg-inline--fa {
  overflow: visible;
}

.svg-inline--fa {
  display: inline-block;
  font-size: inherit;
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.225em;
}
.svg-inline--fa.fa-w-1 {
  width: 0.0625em;
}
.svg-inline--fa.fa-w-2 {
  width: 0.125em;
}
.svg-inline--fa.fa-w-3 {
  width: 0.1875em;
}
.svg-inline--fa.fa-w-4 {
  width: 0.25em;
}
.svg-inline--fa.fa-w-5 {
  width: 0.3125em;
}
.svg-inline--fa.fa-w-6 {
  width: 0.375em;
}
.svg-inline--fa.fa-w-7 {
  width: 0.4375em;
}
.svg-inline--fa.fa-w-8 {
  width: 0.5em;
}
.svg-inline--fa.fa-w-9 {
  width: 0.5625em;
}
.svg-inline--fa.fa-w-10 {
  width: 0.625em;
}
.svg-inline--fa.fa-w-11 {
  width: 0.6875em;
}
.svg-inline--fa.fa-w-12 {
  width: 0.75em;
}
.svg-inline--fa.fa-w-13 {
  width: 0.8125em;
}
.svg-inline--fa.fa-w-14 {
  width: 0.875em;
}
.svg-inline--fa.fa-w-15 {
  width: 0.9375em;
}
.svg-inline--fa.fa-w-16 {
  width: 1em;
}
.svg-inline--fa.fa-w-17 {
  width: 1.0625em;
}
.svg-inline--fa.fa-w-18 {
  width: 1.125em;
}
.svg-inline--fa.fa-w-19 {
  width: 1.1875em;
}
.svg-inline--fa.fa-w-20 {
  width: 1.25em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: 0.3em;
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: 0.3em;
  width: auto;
}
.svg-inline--fa.fa-border {
  height: 1.5em;
}
.svg-inline--fa.fa-li {
  width: 2em;
}
.svg-inline--fa.fa-fw {
  width: 1.25em;
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter {
  background-color: #ff253a;
  border-radius: 1em;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  color: #fff;
  height: 1.5em;
  line-height: 1;
  max-width: 5em;
  min-width: 1.5em;
  overflow: hidden;
  padding: 0.25em;
  right: 0;
  text-overflow: ellipsis;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: 0;
  right: 0;
  top: auto;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: bottom right;
          transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: 0;
  left: 0;
  right: auto;
  top: auto;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: bottom left;
          transform-origin: bottom left;
}

.fa-layers-top-right {
  right: 0;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-top-left {
  left: 0;
  right: auto;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top left;
          transform-origin: top left;
}

.fa-lg {
  font-size: 1.3333333333em;
  line-height: 0.75em;
  vertical-align: -0.0667em;
}

.fa-xs {
  font-size: 0.75em;
}

.fa-sm {
  font-size: 0.875em;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: 2.5em;
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: -2em;
  position: absolute;
  text-align: center;
  width: 2em;
  line-height: inherit;
}

.fa-border {
  border: solid 0.08em #eee;
  border-radius: 0.1em;
  padding: 0.2em 0.25em 0.15em;
}

.fa-pull-left {
  float: left;
}

.fa-pull-right {
  float: right;
}

.fa.fa-pull-left,
.fas.fa-pull-left,
.far.fa-pull-left,
.fal.fa-pull-left,
.fab.fa-pull-left {
  margin-right: 0.3em;
}
.fa.fa-pull-right,
.fas.fa-pull-right,
.far.fa-pull-right,
.fal.fa-pull-right,
.fab.fa-pull-right {
  margin-left: 0.3em;
}

.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear;
}

.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8);
}

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg);
}

.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg);
}

.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg);
}

.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1);
}

.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1);
}

.fa-flip-both, .fa-flip-horizontal.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1);
}

:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical,
:root .fa-flip-both {
  -webkit-filter: none;
          filter: none;
}

.fa-stack {
  display: inline-block;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: #fff;
}

.sr-only {
  border: 0;
  clip: rect(0, 0, 0, 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

.sr-only-focusable:active, .sr-only-focusable:focus {
  clip: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  position: static;
  width: auto;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: 1;
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: 0.4;
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: 0.4;
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: 1;
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}

.fad.fa-inverse {
  color: #fff;
}</style><style type="text/css">svg:not(:root).svg-inline--fa {
  overflow: visible;
}

.svg-inline--fa {
  display: inline-block;
  font-size: inherit;
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.225em;
}
.svg-inline--fa.fa-w-1 {
  width: 0.0625em;
}
.svg-inline--fa.fa-w-2 {
  width: 0.125em;
}
.svg-inline--fa.fa-w-3 {
  width: 0.1875em;
}
.svg-inline--fa.fa-w-4 {
  width: 0.25em;
}
.svg-inline--fa.fa-w-5 {
  width: 0.3125em;
}
.svg-inline--fa.fa-w-6 {
  width: 0.375em;
}
.svg-inline--fa.fa-w-7 {
  width: 0.4375em;
}
.svg-inline--fa.fa-w-8 {
  width: 0.5em;
}
.svg-inline--fa.fa-w-9 {
  width: 0.5625em;
}
.svg-inline--fa.fa-w-10 {
  width: 0.625em;
}
.svg-inline--fa.fa-w-11 {
  width: 0.6875em;
}
.svg-inline--fa.fa-w-12 {
  width: 0.75em;
}
.svg-inline--fa.fa-w-13 {
  width: 0.8125em;
}
.svg-inline--fa.fa-w-14 {
  width: 0.875em;
}
.svg-inline--fa.fa-w-15 {
  width: 0.9375em;
}
.svg-inline--fa.fa-w-16 {
  width: 1em;
}
.svg-inline--fa.fa-w-17 {
  width: 1.0625em;
}
.svg-inline--fa.fa-w-18 {
  width: 1.125em;
}
.svg-inline--fa.fa-w-19 {
  width: 1.1875em;
}
.svg-inline--fa.fa-w-20 {
  width: 1.25em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: 0.3em;
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: 0.3em;
  width: auto;
}
.svg-inline--fa.fa-border {
  height: 1.5em;
}
.svg-inline--fa.fa-li {
  width: 2em;
}
.svg-inline--fa.fa-fw {
  width: 1.25em;
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter {
  background-color: #ff253a;
  border-radius: 1em;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  color: #fff;
  height: 1.5em;
  line-height: 1;
  max-width: 5em;
  min-width: 1.5em;
  overflow: hidden;
  padding: 0.25em;
  right: 0;
  text-overflow: ellipsis;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: 0;
  right: 0;
  top: auto;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: bottom right;
          transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: 0;
  left: 0;
  right: auto;
  top: auto;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: bottom left;
          transform-origin: bottom left;
}

.fa-layers-top-right {
  right: 0;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-top-left {
  left: 0;
  right: auto;
  top: 0;
  -webkit-transform: scale(0.25);
          transform: scale(0.25);
  -webkit-transform-origin: top left;
          transform-origin: top left;
}

.fa-lg {
  font-size: 1.3333333333em;
  line-height: 0.75em;
  vertical-align: -0.0667em;
}

.fa-xs {
  font-size: 0.75em;
}

.fa-sm {
  font-size: 0.875em;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: 2.5em;
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: -2em;
  position: absolute;
  text-align: center;
  width: 2em;
  line-height: inherit;
}

.fa-border {
  border: solid 0.08em #eee;
  border-radius: 0.1em;
  padding: 0.2em 0.25em 0.15em;
}

.fa-pull-left {
  float: left;
}

.fa-pull-right {
  float: right;
}

.fa.fa-pull-left,
.fas.fa-pull-left,
.far.fa-pull-left,
.fal.fa-pull-left,
.fab.fa-pull-left {
  margin-right: 0.3em;
}
.fa.fa-pull-right,
.fas.fa-pull-right,
.far.fa-pull-right,
.fal.fa-pull-right,
.fab.fa-pull-right {
  margin-left: 0.3em;
}

.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear;
}

.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8);
}

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg);
}

.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg);
}

.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg);
}

.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1);
}

.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1);
}

.fa-flip-both, .fa-flip-horizontal.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1);
}

:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical,
:root .fa-flip-both {
  -webkit-filter: none;
          filter: none;
}

.fa-stack {
  display: inline-block;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: #fff;
}

.sr-only {
  border: 0;
  clip: rect(0, 0, 0, 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

.sr-only-focusable:active, .sr-only-focusable:focus {
  clip: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  position: static;
  width: auto;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: 1;
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: 0.4;
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: 0.4;
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: 1;
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}

.fad.fa-inverse {
  color: #fff;
}</style><link rel="icon" href="https://www.jdoodle.com/favicon.ico"><title>Python Online Editor - Python Online IDE -  Python Programming Online</title><script type="text/javascript" async="" src="./minimax_files/recaptcha__pt_br.js.download" crossorigin="anonymous" integrity="sha384-ucJYXpcI+YzgzklSYS0a336oZ63IC0Yi3fww2BiaEfztVzXHaInoskeF7lNIDGMd"></script><script type="application/ld+json">{
        "@context" : "http://schema.org",
        "@type" : "SoftwareApplication",
        "name" : "JDoodle - Online Compiler And Editor",
        "image" : "https://www.jdoodle.com/img/jdoodle.113077a7.png"
      }</script><link href="https://www.jdoodle.com/css/chunk-035abb13.6be68169.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-03fa5ac1.b693584a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-066bfaa8.b693584a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-06ac3a82.57ecb774.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-07b84418.06ba15e0.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-0b949e46.9a64a201.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-0c6b7169.8f64bd2e.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-1c0ee588.bbab49d0.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-1d4bce52.b693584a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-211c311d.9a64a201.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-22bc8f13.b693584a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-280f09d4.b50ebec4.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-283a7498.049be0dc.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-285b3760.82c50a7d.css" rel="prefetch"><link href="./minimax_files/chunk-29065412.84cbf6a8.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-2960dc9a.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-2c123f4a.42e57394.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-36b81d26.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-38b68bed.b84218e7.css" rel="prefetch"><link href="./minimax_files/chunk-3b4ba898.bc28df53.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-3c9ac7f8.e0b6b949.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-3d1dfd18.467687e6.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-4a2a93f2.42e57394.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-4a445de6.d0364b7b.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-4d0f887a.0ab5a017.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-5001cd97.9a64a201.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-51026210.0f23e30b.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-51df5fd4.99a77867.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-527e1f3f.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-558d83ec.c691c68d.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-56f43360.b7eb66c6.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-578b50f5.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-5861a136.fa3c08b2.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-5bc51e22.2dc7e121.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-5c85b6b4.8a8d1b07.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-5e33ccdd.94dbbfc5.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-62fcc2db.c27ca486.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-63be1ceb.1bb7a823.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-6b1c31fe.8c46cdc8.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-6bb96cd4.a1227098.css" rel="prefetch"><link href="./minimax_files/chunk-6c2dba3d.33717b4f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-6de5ffb2.8cee74d3.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-70de9abe.64f853ca.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-716a62d6.08fa1376.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7aac3342.42e57394.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7c8eb802.4804bf7a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7d1ec31c.30def069.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7ea1b17d.ad6e41ed.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7f25d7f6.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-7fc543a6.b693584a.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-8a7c0928.a977731d.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-9723e9d2.1e815cd6.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-9c0e66b8.92a4068e.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-9c86a6bc.5410b7d3.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-9ee35d30.f5ce280f.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-9fe2e7e4.240aa3e5.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-ac8a0d62.42e57394.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-add4b03e.d56167ef.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-c498faba.d060ca09.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-cacedc96.317dfa84.css" rel="prefetch"><link href="./minimax_files/chunk-ccdf3fd2.64f20cc8.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-d468c04c.c2aea914.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-dd1c8980.8e443cb8.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-e0dc81dc.47664179.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-e6f9bb36.06060476.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-f4851822.51383d13.css" rel="prefetch"><link href="https://www.jdoodle.com/css/chunk-fd1c93e0.5f551bff.css" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-035abb13.2c27071e.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-03fa5ac1.253fdbc9.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-066bfaa8.ac58731b.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-06ac3a82.60a77db5.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-07b84418.81e8869b.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-0b949e46.029503c4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-0c6b7169.447f57cb.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-1c0ee588.8e16b614.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-1d4bce52.87d9a97f.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-211c311d.ad1ab5f4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-22bc8f13.f7e2bbc9.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-251e2180.25d4c791.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-280f09d4.a4abb862.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-283a7498.fc2fd8c4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-285b3760.a42ee058.js" rel="prefetch"><link href="./minimax_files/chunk-29065412.044c215a.js.download" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-2960dc9a.b94a1523.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-2b7aad2e.77f84cbf.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-2c123f4a.879a8c16.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-2d0f028f.8a6118e6.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-36b81d26.e9ebf26f.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-38b68bed.d7ec3706.js" rel="prefetch"><link href="./minimax_files/chunk-3b4ba898.2783ef8b.js.download" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-3c9ac7f8.4ea803f4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-3d1dfd18.0b84cbca.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-4a2a93f2.3264ae9b.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-4a445de6.50edeacb.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-4d0f887a.aad67589.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5001cd97.e2178a13.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-51026210.c2d1488c.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-51df5fd4.73701e66.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-527e1f3f.4521399a.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-558d83ec.115c3046.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-56f43360.ccc6ad80.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-578b50f5.56b33eef.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5861a136.96d7ce67.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5bc51e22.1e8adbad.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5c504b38.540480a1.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5c85b6b4.c50b52a3.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-5e33ccdd.8119a800.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-62fcc2db.2142a1d2.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-63be1ceb.4bb0eab4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-6b1c31fe.ccfa561d.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-6bb96cd4.d778ad3d.js" rel="prefetch"><link href="./minimax_files/chunk-6c2dba3d.c0540bce.js.download" rel="prefetch"><link href="./minimax_files/chunk-6cf5e006.bd016028.js.download" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-6de5ffb2.c376a3b9.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-70de9abe.9c639882.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-716a62d6.677786da.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7aac3342.10ccde0f.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7c8eb802.58951da2.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7d1ec31c.d88e5c0e.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7db688a6.250c5b5e.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7ea1b17d.d6646ae3.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7f25d7f6.1fdc5982.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-7fc543a6.07c01db9.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-8a7c0928.be6fed9c.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-9723e9d2.86b8c5da.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-9c0e66b8.1eb6b751.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-9c86a6bc.664886cb.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-9ee35d30.a12cf71a.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-9fe2e7e4.563de391.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-ac8a0d62.219782cc.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-add4b03e.e72aafc8.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-c498faba.03d584cc.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-cacedc96.85a8d13d.js" rel="prefetch"><link href="./minimax_files/chunk-ccdf3fd2.33911966.js.download" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-d468c04c.6b2d693d.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-dd1c8980.36827ff2.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-e0dc81dc.734c3d1e.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-e6f9bb36.4e899ca4.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-f4851822.2845aa76.js" rel="prefetch"><link href="https://www.jdoodle.com/js/chunk-fd1c93e0.2eff9b68.js" rel="prefetch"><link href="./minimax_files/app.38c45ee0.css" rel="preload" as="style"><link href="./minimax_files/chunk-vendors.9d5e62ae.css" rel="preload" as="style"><link href="./minimax_files/app.87c94515.js.download" rel="preload" as="script"><link href="./minimax_files/chunk-vendors.efd56467.js.download" rel="preload" as="script"><link href="./minimax_files/chunk-vendors.9d5e62ae.css" rel="stylesheet"><link href="./minimax_files/app.38c45ee0.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="./minimax_files/chunk-ccdf3fd2.64f20cc8.css"><script charset="utf-8" src="./minimax_files/chunk-ccdf3fd2.33911966.js.download"></script><link rel="stylesheet" type="text/css" href="./minimax_files/chunk-6c2dba3d.33717b4f.css"><script charset="utf-8" src="./minimax_files/chunk-6c2dba3d.c0540bce.js.download"></script><style type="text/css">.Cookie{position:fixed;overflow:hidden;box-sizing:border-box;z-index:9999;width:100%;display:flex;justify-content:space-between;align-items:baseline;flex-direction:column}.Cookie>*{margin:.9375rem 0;align-self:center}@media screen and (min-width: 48rem){.Cookie{flex-flow:row}.Cookie>*{margin:0}}.Cookie--top{top:0;left:0;right:0}.Cookie--bottom{bottom:0;left:0;right:0}.Cookie__buttons{display:flex;flex-direction:column}.Cookie__buttons>*{margin:.3125rem 0}@media screen and (min-width: 48rem){.Cookie__buttons{flex-direction:row}.Cookie__buttons>*{margin:0 .9375rem}}.Cookie__button{cursor:pointer;align-self:center;white-space:nowrap}.Cookie__declineButton{cursor:pointer;align-self:center;white-space:nowrap}.Cookie--base{background:#F1F1F1;color:#232323;padding:1.250em}.Cookie--base .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--base .Cookie__button:hover{background:#7ebf36}.Cookie--base .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#727272;border-radius:0;border:0;font-size:1em}.Cookie--base .Cookie__button--decline:hover{background:#cbcbcb}.Cookie--base--rounded{background:#F1F1F1;color:#232323;padding:1.250em}.Cookie--base--rounded .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--base--rounded .Cookie__button:hover{background:#7ebf36}.Cookie--base--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#727272;border-radius:20px;border:0;font-size:1em}.Cookie--base--rounded .Cookie__button--decline:hover{background:#cbcbcb}.Cookie--blood-orange{background:#424851;color:#fff;padding:1.250em}.Cookie--blood-orange .Cookie__button{background:#E76A68;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--blood-orange .Cookie__button:hover{background:#e03f3c}.Cookie--blood-orange .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:0;border:0;font-size:1em}.Cookie--blood-orange .Cookie__button--decline:hover{background:#202327}.Cookie--blood-orange--rounded{background:#424851;color:#fff;padding:1.250em}.Cookie--blood-orange--rounded .Cookie__button{background:#E76A68;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--blood-orange--rounded .Cookie__button:hover{background:#e03f3c}.Cookie--blood-orange--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:20px;border:0;font-size:1em}.Cookie--blood-orange--rounded .Cookie__button--decline:hover{background:#202327}.Cookie--dark-lime{background:#424851;color:#fff;padding:1.250em}.Cookie--dark-lime .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--dark-lime .Cookie__button:hover{background:#7ebf36}.Cookie--dark-lime .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:0;border:0;font-size:1em}.Cookie--dark-lime .Cookie__button--decline:hover{background:#202327}.Cookie--dark-lime--rounded{background:#424851;color:#fff;padding:1.250em}.Cookie--dark-lime--rounded .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--dark-lime--rounded .Cookie__button:hover{background:#7ebf36}.Cookie--dark-lime--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:20px;border:0;font-size:1em}.Cookie--dark-lime--rounded .Cookie__button--decline:hover{background:#202327}.Cookie--royal{background:#FBC227;color:#232323;padding:1.250em}.Cookie--royal .Cookie__button{background:#726CEA;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--royal .Cookie__button:hover{background:#473fe4}.Cookie--royal .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#221901;border-radius:0;border:0;font-size:1em}.Cookie--royal .Cookie__button--decline:hover{background:#d29a04}.Cookie--royal--rounded{background:#FBC227;color:#232323;padding:1.250em}.Cookie--royal--rounded .Cookie__button{background:#726CEA;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--royal--rounded .Cookie__button:hover{background:#473fe4}.Cookie--royal--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#221901;border-radius:20px;border:0;font-size:1em}.Cookie--royal--rounded .Cookie__button--decline:hover{background:#d29a04}.slideFromTop-enter,.slideFromTop-leave-to{transform:translate(0px, -12.5em)}.slideFromTop-enter-to,.slideFromTop-leave{transform:translate(0px, 0px)}.slideFromBottom-enter,.slideFromBottom-leave-to{transform:translate(0px, 12.5em)}.slideFromBottom-enter-to,.slideFromBottom-leave{transform:translate(0px, 0px)}.slideFromBottom-enter-active,.slideFromBottom-leave-active,.slideFromTop-enter-active,.slideFromTop-leave-active{transition:transform .4s ease-in}.fade-enter-active,.fade-leave-active{transition:opacity .5s}.fade-enter,.fade-leave-to{opacity:0}
</style><style type="text/css">.Cookie{position:fixed;overflow:hidden;box-sizing:border-box;z-index:9999;width:100%;display:flex;justify-content:space-between;align-items:baseline;flex-direction:column}.Cookie>*{margin:.9375rem 0;align-self:center}@media screen and (min-width: 48rem){.Cookie{flex-flow:row}.Cookie>*{margin:0}}.Cookie--top{top:0;left:0;right:0}.Cookie--bottom{bottom:0;left:0;right:0}.Cookie__buttons{display:flex;flex-direction:column}.Cookie__buttons>*{margin:.3125rem 0}@media screen and (min-width: 48rem){.Cookie__buttons{flex-direction:row}.Cookie__buttons>*{margin:0 .9375rem}}.Cookie__button{cursor:pointer;align-self:center;white-space:nowrap}.Cookie__declineButton{cursor:pointer;align-self:center;white-space:nowrap}.Cookie--base{background:#F1F1F1;color:#232323;padding:1.250em}.Cookie--base .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--base .Cookie__button:hover{background:#7ebf36}.Cookie--base .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#727272;border-radius:0;border:0;font-size:1em}.Cookie--base .Cookie__button--decline:hover{background:#cbcbcb}.Cookie--base--rounded{background:#F1F1F1;color:#232323;padding:1.250em}.Cookie--base--rounded .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--base--rounded .Cookie__button:hover{background:#7ebf36}.Cookie--base--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#727272;border-radius:20px;border:0;font-size:1em}.Cookie--base--rounded .Cookie__button--decline:hover{background:#cbcbcb}.Cookie--blood-orange{background:#424851;color:#fff;padding:1.250em}.Cookie--blood-orange .Cookie__button{background:#E76A68;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--blood-orange .Cookie__button:hover{background:#e03f3c}.Cookie--blood-orange .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:0;border:0;font-size:1em}.Cookie--blood-orange .Cookie__button--decline:hover{background:#202327}.Cookie--blood-orange--rounded{background:#424851;color:#fff;padding:1.250em}.Cookie--blood-orange--rounded .Cookie__button{background:#E76A68;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--blood-orange--rounded .Cookie__button:hover{background:#e03f3c}.Cookie--blood-orange--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:20px;border:0;font-size:1em}.Cookie--blood-orange--rounded .Cookie__button--decline:hover{background:#202327}.Cookie--dark-lime{background:#424851;color:#fff;padding:1.250em}.Cookie--dark-lime .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--dark-lime .Cookie__button:hover{background:#7ebf36}.Cookie--dark-lime .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:0;border:0;font-size:1em}.Cookie--dark-lime .Cookie__button--decline:hover{background:#202327}.Cookie--dark-lime--rounded{background:#424851;color:#fff;padding:1.250em}.Cookie--dark-lime--rounded .Cookie__button{background:#97D058;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--dark-lime--rounded .Cookie__button:hover{background:#7ebf36}.Cookie--dark-lime--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#000;border-radius:20px;border:0;font-size:1em}.Cookie--dark-lime--rounded .Cookie__button--decline:hover{background:#202327}.Cookie--royal{background:#FBC227;color:#232323;padding:1.250em}.Cookie--royal .Cookie__button{background:#726CEA;padding:0.625em 3.125em;color:#fff;border-radius:0;border:0;font-size:1em}.Cookie--royal .Cookie__button:hover{background:#473fe4}.Cookie--royal .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#221901;border-radius:0;border:0;font-size:1em}.Cookie--royal .Cookie__button--decline:hover{background:#d29a04}.Cookie--royal--rounded{background:#FBC227;color:#232323;padding:1.250em}.Cookie--royal--rounded .Cookie__button{background:#726CEA;padding:0.625em 3.125em;color:#fff;border-radius:20px;border:0;font-size:1em}.Cookie--royal--rounded .Cookie__button:hover{background:#473fe4}.Cookie--royal--rounded .Cookie__button--decline{background:transparent;padding:0.625em 3.125em;color:#221901;border-radius:20px;border:0;font-size:1em}.Cookie--royal--rounded .Cookie__button--decline:hover{background:#d29a04}.slideFromTop-enter,.slideFromTop-leave-to{transform:translate(0px, -12.5em)}.slideFromTop-enter-to,.slideFromTop-leave{transform:translate(0px, 0px)}.slideFromBottom-enter,.slideFromBottom-leave-to{transform:translate(0px, 12.5em)}.slideFromBottom-enter-to,.slideFromBottom-leave{transform:translate(0px, 0px)}.slideFromBottom-enter-active,.slideFromBottom-leave-active,.slideFromTop-enter-active,.slideFromTop-leave-active{transition:transform .4s ease-in}.fade-enter-active,.fade-leave-active{transition:opacity .5s}.fade-enter,.fade-leave-to{opacity:0}
</style><meta name="description" content="Python Online Editor - Python Online IDE -  Python Programming Online - Share Save Python Program online" data-vue-router-controlled=""><meta name="keywords" content="Python Online Editor - Python Online IDE -  Python Programming Online - Share Save Python Program online" data-vue-router-controlled=""><script charset="utf-8" src="./minimax_files/chunk-6cf5e006.bd016028.js.download"></script><link rel="stylesheet" type="text/css" href="./minimax_files/chunk-3b4ba898.bc28df53.css"><script charset="utf-8" src="./minimax_files/chunk-3b4ba898.2783ef8b.js.download"></script><link rel="stylesheet" type="text/css" href="./minimax_files/chunk-29065412.84cbf6a8.css"><script charset="utf-8" src="./minimax_files/chunk-29065412.044c215a.js.download"></script><script async="" src="./minimax_files/saved_resource" data-rq="7bfdefba-8710-41b3-98d1-a635291d5833" id="escid6303"></script><script type="text/javascript" src="./minimax_files/prebid3.js.download" async=""></script><link href="./minimax_files/gpt.js.download" as="script" rel="prefetch"><script src="./minimax_files/theme-gruvbox.js.download"></script><script src="./minimax_files/mode-python.js.download"></script><link href="https://s.flocdn.com/cmp/2.1.5/tcf-2.0-loader.js" as="script" rel="preload"><link href="https://s.flocdn.com/cmp/2.1.5/tcf-2.0-cmp.js" as="script" rel="preload"><script type="text/javascript" src="./minimax_files/gpt.js.download"></script><meta http-equiv="origin-trial" content="AzoawhTRDevLR66Y6MROu167EDncFPBvcKOaQispTo9ouEt5LvcBjnRFqiAByRT+2cDHG1Yj4dXwpLeIhc98/gIAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjYxMjk5MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A6+nc62kbJgC46ypOwRsNW6RkDn2x7tgRh0wp7jb3DtFF7oEhu1hhm4rdZHZ6zXvnKZLlYcBlQUImC4d3kKihAcAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjYxMjk5MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A/9La288e7MDEU2ifusFnMg1C2Ij6uoa/Z/ylwJIXSsWfK37oESIPbxbt4IU86OGqDEPnNVruUiMjfKo65H/CQwAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjYxMjk5MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script src="./minimax_files/pubads_impl_2022071101.js.download" async=""></script><link rel="preload" href="./minimax_files/f.txt" as="script"><script type="text/javascript" src="./minimax_files/f.txt"></script><link rel="preload" href="./minimax_files/f(1).txt" as="script"><script type="text/javascript" src="./minimax_files/f(1).txt"></script><script esp-signal="true" src="./minimax_files/esp.js.download"></script></head><body><noscript><strong>We're sorry but jdoodle-spa doesn't work properly without JavaScript enabled. Please enable it to continue.</strong></noscript><div id="app" class="dark"><nav data-v-368b6c3e="" class="jd-nav is-marginless" msg="Welcome to JDoodle.com"><div data-v-368b6c3e="" class="level is-mobile is-marginless"><div data-v-368b6c3e="" class="level-left"><div data-v-368b6c3e="" class="level-item is-vertical"><a data-v-368b6c3e="" href="https://www.jdoodle.com/" class="router-link-active"><img data-v-368b6c3e="" src="./minimax_files/jdoodle-dark.57dced51.png" alt="JDoodle" width="150" class="logo"></a></div></div><div data-v-368b6c3e="" class="level-right is-hidden-print"><div data-v-368b6c3e="" class="level-item"><button data-v-368b6c3e="" class="button share-button is-rounded"><svg data-v-368b6c3e="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="share" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="share-button-icon svg-inline--fa fa-share fa-w-16"><path data-v-368b6c3e="" fill="currentColor" d="M503.691 189.836L327.687 37.851C312.281 24.546 288 35.347 288 56.015v80.053C127.371 137.907 0 170.1 0 322.326c0 61.441 39.581 122.309 83.333 154.132 13.653 9.931 33.111-2.533 28.077-18.631C66.066 312.814 132.917 274.316 288 272.085V360c0 20.7 24.3 31.453 39.687 18.164l176.004-152c11.071-9.562 11.086-26.753 0-36.328z" class=""></path></svg></button></div><div data-v-368b6c3e="" class="level-item"><button data-v-368b6c3e="" class="button user-button is-rounded"><svg data-v-368b6c3e="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="bars" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="share-button-icon svg-inline--fa fa-bars fa-w-14"><path data-v-368b6c3e="" fill="currentColor" d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z" class=""></path></svg></button></div><div data-v-368b6c3e="" class="level-item"><button data-v-368b6c3e="" class="button is-info has-text-white sign-in-button"><strong data-v-368b6c3e="">Sign In</strong></button><!----></div></div></div><!----></nav><div class="app-wrap"><div data-v-591f97f5="" class="home-container full-screen dark"><div data-v-591f97f5="" class="has-text-centered title-section is-marginless"><h1 data-v-591f97f5="" class="title is-marginless custom-grey"><span data-v-591f97f5="">Online</span> Python 3 <!----><span data-v-591f97f5=""> IDE</span></h1><!----></div><!----><!----><!----><div data-v-591f97f5="" class="box no-border-print code-editor-box columns"><div data-v-591f97f5="" id="ide-left" class="ide-left split" style="width: calc(60% - 5px);"><!----><div data-v-591f97f5="" class="is-flex ide-part is-mobile"><!----><div data-v-591f97f5="" id="ide-code" class="split is-marginless is-paddingless"><!----><div data-v-591f97f5="" id="code" class="code-editor no-border-print ace_editor ace-gruvbox ace_dark" style="font-size: 12px; height: 698.889px;" draggable="false"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 238px; left: 241px;"></textarea><div class="ace_gutter" aria-hidden="true" style="display: block; left: 0px; width: 47px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 0px; left: 0px; width: 47px;"><div class="ace_gutter-cell " style="height: 14px; top: 0px;">1<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 14px;">2<span style="display: none; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 28px;">3<span style="display: inline-block; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 42px;">4<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 56px;">5<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 70px;">6<span style="display: inline-block; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 84px;">7<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 98px;">8<span style="display: inline-block; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 112px;">9<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 126px;">10<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 140px;">11<span style="display: inline-block; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 154px;">12<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 168px;">13<span style="display: inline-block; height: 14px;" class="ace_fold-widget ace_start ace_open"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 182px;">14<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 196px;">15<span style="display: none;"></span></div><div class="ace_gutter-cell " style="height: 14px; top: 210px;">16<span style="display: none;"></span></div><div class="ace_gutter-cell ace_gutter-active-line " style="height: 14px; top: 224px;">17<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 14px; left: 46.1797px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 0px; left: 0px; width: 808.82px; height: 725px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 531px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 14px; top: 224px; left: 0px; right: 0px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 14px; width: 6.58984px; top: 224px; left: 188.516px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 14px; width: 6.58984px; top: 224px; left: 50.1289px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line" style="height: 14px; top: 0px;"><span class="ace_identifier">INF</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_constant ace_numeric">1e9</span><span class="ace_keyword ace_operator">+</span><span class="ace_constant ace_numeric">17</span></div><div class="ace_line" style="height: 14px; top: 14px;"><span class="ace_identifier">matriz</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_paren ace_lparen">[[</span><span class="ace_string">' '</span>, <span class="ace_string">' '</span>, <span class="ace_string">' '</span><span class="ace_paren ace_rparen">]</span>, <span class="ace_paren ace_lparen">[</span><span class="ace_string">' '</span>, <span class="ace_string">' '</span>, <span class="ace_string">' '</span><span class="ace_paren ace_rparen">]</span>, <span class="ace_paren ace_lparen">[</span><span class="ace_string">' '</span>, <span class="ace_string">' '</span>, <span class="ace_string">' '</span><span class="ace_paren ace_rparen">]]</span></div><div class="ace_line" style="height: 14px; top: 28px;"><span class="ace_keyword">def</span> <span class="ace_identifier">minimax</span><span class="ace_paren ace_lparen">(</span> <span class="ace_identifier">board</span>, <span class="ace_identifier">depth</span>, <span class="ace_identifier">maximizingPlayer</span><span class="ace_paren ace_rparen">)</span>:</div><div class="ace_line" style="height: 14px; top: 42px;">    <span class="ace_keyword">if</span> <span class="ace_identifier">depth</span> <span class="ace_keyword ace_operator">==</span> <span class="ace_constant ace_numeric">0</span> <span class="ace_keyword">or</span> <span class="ace_identifier">idBoardFull</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">board</span><span class="ace_paren ace_rparen">)</span><span class="ace_comment">#node is a terminal node then</span></div><div class="ace_line" style="height: 14px; top: 56px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">boardValue</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">board</span><span class="ace_paren ace_rparen">)</span><span class="ace_comment"># the heuristic value of node</span></div><div class="ace_line" style="height: 14px; top: 70px;">    <span class="ace_keyword">if</span> <span class="ace_identifier">maximizingPlayer</span>:</div><div class="ace_line" style="height: 14px; top: 84px;"><span class="ace_indent-guide">    </span>    <span class="ace_identifier">value</span> <span class="ace_keyword ace_operator">=</span> −<span class="ace_identifier">INF</span></div><div class="ace_line" style="height: 14px; top: 98px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">for</span> <span class="ace_identifier">child</span> <span class="ace_keyword">in</span> <span class="ace_identifier">generatePossibleBoard</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">board</span>, <span class="ace_identifier">maximizingPlayer</span><span class="ace_paren ace_rparen">)</span>:<span class="ace_comment">#each child of node do</span></div><div class="ace_line" style="height: 14px; top: 112px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">value</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_support ace_function">max</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">value</span>, <span class="ace_identifier">minimax</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">child</span>, <span class="ace_identifier">depth</span> − <span class="ace_constant ace_numeric">1</span>, <span class="ace_identifier">FALSE</span><span class="ace_paren ace_rparen">))</span></div><div class="ace_line" style="height: 14px; top: 126px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">value</span></div><div class="ace_line" style="height: 14px; top: 140px;">    <span class="ace_keyword">else</span>: <span class="ace_comment">#(* minimizing player *)</span></div><div class="ace_line" style="height: 14px; top: 154px;"><span class="ace_indent-guide">    </span>    <span class="ace_identifier">value</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_identifier">INF</span></div><div class="ace_line" style="height: 14px; top: 168px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">for</span> <span class="ace_identifier">each</span> <span class="ace_identifier">child</span> <span class="ace_keyword">in</span> <span class="ace_identifier">generatePossibleBoard</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">board</span>, <span class="ace_identifier">maximizingPlayer</span><span class="ace_paren ace_rparen">)</span>: <span class="ace_comment">#of node do</span></div><div class="ace_line" style="height: 14px; top: 182px;"><span class="ace_indent-guide">    </span><span class="ace_indent-guide">    </span>    <span class="ace_identifier">value</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_support ace_function">min</span><span class="ace_paren ace_lparen">(</span> <span class="ace_identifier">value</span>, <span class="ace_identifier">minimax</span><span class="ace_paren ace_lparen">(</span> <span class="ace_identifier">child</span>, <span class="ace_identifier">depth</span> − <span class="ace_constant ace_numeric">1</span>, <span class="ace_identifier">TRUE</span> <span class="ace_paren ace_rparen">)</span> <span class="ace_paren ace_rparen">)</span></div><div class="ace_line" style="height: 14px; top: 196px;"><span class="ace_indent-guide">    </span>    <span class="ace_keyword">return</span> <span class="ace_identifier">value</span></div><div class="ace_line" style="height: 14px; top: 210px;"></div><div class="ace_line" style="height: 14px; top: 224px;"><span class="ace_identifier">minimax</span><span class="ace_paren ace_lparen">(</span> <span class="ace_identifier">board</span>, <span class="ace_identifier">depth</span>, <span class="ace_identifier">TRUE</span> <span class="ace_paren ace_rparen">)</span></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 224px; left: 195px; width: 7px; height: 14px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 22px; height: 238px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 46.1797px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 815px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></div></div></div><div class="gutter gutter-horizontal" style="width: 10px;"></div><div data-v-591f97f5="" id="ide-right" class="ide-right split" style="width: calc(40% - 5px);"><section data-v-591f97f5="" class="accordions"><article data-v-591f97f5="" class="accordion is-active"><div data-v-591f97f5="" class="accordion-header toggle background-grey-light has-text-weight-semibold"><p data-v-591f97f5=""><svg data-v-591f97f5="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="chevron-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-chevron-down fa-w-14"><path data-v-591f97f5="" fill="currentColor" d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z" class=""></path></svg>&nbsp;&nbsp;&nbsp;Execute Mode, Version, Inputs &amp; Arguments</p></div><div data-v-591f97f5="" class="accordion-body custom-grey"><div data-v-591f97f5="" class="accordion-content is-paddingless"><div data-v-591f97f5="" class="columns is-multiline options-section is-marginless padding-left-none"><div data-v-591f97f5="" class="column columns is-multiline left-column is-marginless padding-left-none is-print-12 is-6"><div data-v-591f97f5="" class="column is-hidden-print is-12"><div data-v-591f97f5="" class="version-interactive-section is-mobile"><div data-v-591f97f5="" class="has-text-centered"><div data-v-591f97f5="" class="field is-narrow"><div data-v-591f97f5="" class="select is-rounded is-small has-text-weight-bold version-dropdown"><select data-v-591f97f5=""><option data-v-591f97f5="" value="0">
                                  3.5.1
                                </option><option data-v-591f97f5="" value="1">
                                   3.6.3
                                </option><option data-v-591f97f5="" value="2">
                                  3.6.5
                                </option><option data-v-591f97f5="" value="3">
                                  3.7.4
                                </option><option data-v-591f97f5="" value="4">
                                  3.9.9
                                </option></select></div></div></div><div data-v-591f97f5="" class="field has-text-centered"><input data-v-591f97f5="" id="interactiveMode" type="checkbox" name="interactiveMode" class="switch has-text-white"><label data-v-591f97f5="" for="interactiveMode" class="ide-title has-text-weight-semibold">Interactive</label></div></div></div><div data-v-591f97f5="" class="column padding-left-none is-print-12 is-12"><div data-v-591f97f5="" class="column is-12 is-print-12"><div data-v-591f97f5="" class="has-text-weight-semibold ide-title">CommandLine Arguments</div><div data-v-591f97f5="" class="control"><input data-v-591f97f5="" type="text" name="arguments" autocomplete="off" class="input"></div></div></div></div><div data-v-591f97f5="" class="column is-6 is-print-12"><div data-v-591f97f5="" class="has-text-weight-semibold ide-title">Stdin Inputs</div><div data-v-591f97f5="" class="control"><textarea data-v-591f97f5="" rows="2" name="stdin" class="textarea"></textarea></div></div></div></div></div></article></section><div data-v-591f97f5="" class="level execute-section is-hidden-print"><div data-v-591f97f5="" class="level-item"><div data-v-591f97f5="" class="field is-grouped"><p data-v-591f97f5="" class="control"><button data-v-591f97f5="" class="button is-info has-text-white has-text-weight-bold"><span data-v-591f97f5=""><svg data-v-591f97f5="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-play fa-w-14"><path data-v-591f97f5="" fill="currentColor" d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z" class=""></path></svg>&nbsp;&nbsp;&nbsp;Execute</span><!----></button></p><div data-v-591f97f5="" id="ideContainer" data-size="invisible" data-sitekey="6LfPlOsUAAAAAIALEFUM1022nNwsyWjpATeuYMdi" data-badge="inline" class="g-recaptcha is-hidden-print captcha-box"><div class="grecaptcha-badge" data-style="inline" style="width: 256px; height: 60px; box-shadow: gray 0px 0px 5px;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" src="./minimax_files/anchor.html" width="256" height="60" role="presentation" name="a-iwnbz6rwtfmt" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./minimax_files/saved_resource.html"></iframe></div><!----><!----><p data-v-591f97f5="" class="control"><label data-v-591f97f5="" id="upload-button" class="button execute-button"><input data-v-591f97f5="" type="file" name="file" title="" class="file-input upload-pointer"><svg data-v-591f97f5="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="file-upload" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="svg-inline--fa fa-file-upload fa-w-12"><path data-v-591f97f5="" fill="currentColor" d="M224 136V0H24C10.7 0 0 10.7 0 24v464c0 13.3 10.7 24 24 24h336c13.3 0 24-10.7 24-24V160H248c-13.2 0-24-10.8-24-24zm65.18 216.01H224v80c0 8.84-7.16 16-16 16h-32c-8.84 0-16-7.16-16-16v-80H94.82c-14.28 0-21.41-17.29-11.27-27.36l96.42-95.7c6.65-6.61 17.39-6.61 24.04 0l96.42 95.7c10.15 10.07 3.03 27.36-11.25 27.36zM377 105L279.1 7c-4.5-4.5-10.6-7-17-7H256v128h128v-6.1c0-6.3-2.5-12.4-7-16.9z" class=""></path></svg></label></p><p data-v-591f97f5="" class="control"><button data-v-591f97f5="" class="button has-text-dark has-text-weight-bold"><svg data-v-591f97f5="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="ellipsis-h" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="svg-inline--fa fa-ellipsis-h fa-w-16"><path data-v-591f97f5="" fill="currentColor" d="M328 256c0 39.8-32.2 72-72 72s-72-32.2-72-72 32.2-72 72-72 72 32.2 72 72zm104-72c-39.8 0-72 32.2-72 72s32.2 72 72 72 72-32.2 72-72-32.2-72-72-72zm-352 0c-39.8 0-72 32.2-72 72s32.2 72 72 72 72-32.2 72-72-32.2-72-72-72z" class=""></path></svg></button></p><p data-v-591f97f5="" class="control is-hidden-mobile"><button data-v-591f97f5="" class="button has-text-dark has-text-weight-bold"><!----><svg data-v-591f97f5="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="compress" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-compress fa-w-14"><path data-v-591f97f5="" fill="currentColor" d="M436 192H312c-13.3 0-24-10.7-24-24V44c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v84h84c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12zm-276-24V44c0-6.6-5.4-12-12-12h-40c-6.6 0-12 5.4-12 12v84H12c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h124c13.3 0 24-10.7 24-24zm0 300V344c0-13.3-10.7-24-24-24H12c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h84v84c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12zm192 0v-84h84c6.6 0 12-5.4 12-12v-40c0-6.6-5.4-12-12-12H312c-13.3 0-24 10.7-24 24v124c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12z" class=""></path></svg></button></p></div></div></div><div data-v-591f97f5="" class="upload-message has-text-centered" style="display: none;">
          
        </div><div data-v-62a83e41="" data-v-591f97f5="" class="has-text-centered error-box" style="display: none;"><svg data-v-62a83e41="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="exclamation-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="is-size-5 svg-inline--fa fa-exclamation-circle fa-w-16 has-text-danger"><path data-v-62a83e41="" fill="currentColor" d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zm-248 50c-25.405 0-46 20.595-46 46s20.595 46 46 46 46-20.595 46-46-20.595-46-46-46zm-43.673-165.346l7.418 136c.347 6.364 5.609 11.346 11.982 11.346h48.546c6.373 0 11.635-4.982 11.982-11.346l7.418-136c.375-6.874-5.098-12.654-11.982-12.654h-63.383c-6.884 0-12.356 5.78-11.981 12.654z" class=""></path></svg><span data-v-62a83e41="" class="has-text-weight-bold error-message">
        
  </span></div><div data-v-591f97f5="" class="has-text-weight-semibold ide-title">Result</div><div data-v-591f97f5="" class="execute-time level is-mobile is-marginless" style="display: none;"><div data-v-591f97f5="" class="level-left is-marginless is-paddingless"><span data-v-591f97f5="">CPU Time: 0 sec(s), Memory: 0 kilobyte(s)</span></div><div data-v-591f97f5="" class="is-marginless is-paddingless level-right"><!---->executed in  sec(s)</div></div><div data-v-591f97f5=""><div data-v-591f97f5="" id="output" class="code-editor no-border-print ace_editor ace-gruvbox ace_dark" style="height: 52.2222px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 34px; left: 20px;"></textarea><div class="ace_gutter" aria-hidden="true" style="display: none; left: 0px; width: 40px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 20px; left: 0px; width: 40px;"><div class="ace_gutter-cell ace_gutter-active-line " style="height: 14px; top: 0px;">1<span style="display: none;"></span></div></div></div><div class="ace_scroller" style="line-height: 14px; left: 0px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 20px; left: 0px; width: 554px; height: 126px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 547px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 14px; top: 0px; left: 0px; right: 0px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 20px; top: 0px; left: 0px;"><div class="ace_line" style="height: 14px; top: 0px;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 0px; left: 20px; width: 7px; height: 14px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 22px; height: 54px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 0px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 554px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></div><!----><!----></div><!----></div><div data-v-591f97f5="" class="level margin-top-20px"><div data-v-591f97f5="" id="vuukle-ad-5" class="level-item" style="min-width: 300px; min-height: 250px;"><div class="vuukle-ads" style="display: block;height: auto;margin: 0px auto;text-align: center;clear: both; width: 100%; max-width: 100%; overflow: hidden;"><div id="div-gpt-ad-1497448474263-5" data-google-query-id="CK7y5Yja-_gCFSevlQIdyMMBHw"><div id="google_ads_iframe_/213794966,21668329608/vuukle-widget/jdoodle.com-5_0__container__" style="border: 0pt none; margin: auto; text-align: center; width: 336px; height: 280px;"><iframe frameborder="0" src="./minimax_files/container.html" id="google_ads_iframe_/213794966,21668329608/vuukle-widget/jdoodle.com-5_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="336" height="280" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" role="region" aria-label="Advertisement" tabindex="0" data-google-container-id="2" style="border: 0px; vertical-align: bottom; width: 336px !important; height: 280px !important;" data-load-complete="true"></iframe></div></div><div class="vuukle-ad-label" style="display: flex; justify-content: space-evenly; align-items: flex-end; flex-basis: 100%; margin: 0px auto; width: 336px; height: 11px; padding: 0px; line-height: 1.1 !important;"><span style="display: block;margin: 0px;line-height: 0 !important;padding: 0px;"><a aria-label="Vuukle" href="https://vuukle.com/" target="_blank" style="background-color: transparent; box-shadow: none;" rel="noopener nofollow">
  <svg width="11px" viewBox="0 0 30 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
      <g transform="translate(-150.000000, -31.000000)" fill-rule="nonzero">
        <g transform="translate(150.000000, 31.000000)">
          <path d="M41.8097027,29.0691892 L42.3657568,29.0691892 L54.204,1.80093081 L48.8013243,1.80093081 L44.2726216,12.2153514 C43.2397297,14.5605405 42.2069189,18.3368108 42.2069189,18.3368108 C42.2069189,18.3368108 41.1342973,14.5208108 40.1014865,12.2153514 L35.4535946,1.80093081 L29.4948649,1.80093081 L41.8097027,29.0691892 Z M59.7741892,29.1883784 C62.118,29.1883784 64.0645946,28.0754595 65.0974054,26.0481892 L64.9782162,28.8307297 L70.3412432,28.8307297 L70.3412432,11.8972703 L64.9782162,11.8972703 L64.9782162,20.9602703 C64.9782162,23.1067297 63.7864865,24.339 61.6413243,24.339 C59.7345405,24.339 58.8207568,23.226 58.8207568,21.318 L58.8207568,11.8972703 L53.4578919,11.8972703 L53.4578919,21.6757297 C53.4578919,26.4854595 56.0797297,29.1883784 59.7741892,29.1883784 Z M80.7617838,29.1883784 C83.1056757,29.1883784 85.0524324,28.0754595 86.0845946,26.0481892 L85.9662162,28.8307297 L91.3289189,28.8307297 L91.3289189,11.8972703 L85.9662162,11.8972703 L85.9662162,20.9602703 C85.9662162,23.1067297 84.7743243,24.339 82.6289189,24.339 C80.7218919,24.339 79.8081892,23.226 79.8081892,21.318 L79.8081892,11.8972703 L74.4458919,11.8972703 L74.4458919,21.6757297 C74.4458919,26.4854595 77.0671622,29.1883784 80.7617838,29.1883784 Z M100.915946,23.9414595 L102.345405,22.431 L106.556757,28.8307297 L112.793514,28.8307297 L106.158649,18.8138108 L112.157838,11.8972703 L106.198378,11.8972703 L100.637838,18.4162703 C100.796757,17.343 100.915946,16.0312703 100.915946,14.7592703 L100.915946,0.131416216 L95.5524324,0.131416216 L95.5524324,28.8307297 L100.915946,28.8307297 L100.915946,23.9414595 Z M115.301351,28.8307297 L120.624324,28.8307297 L120.624324,0.131416216 L115.301351,0.131416216 L115.301351,28.8307297 Z M129.844865,21.9937297 L142.675946,21.9937297 C143.073243,16.071 139.776486,11.5395405 133.697838,11.5395405 C128.454324,11.5395405 124.362973,15.1965405 124.362973,20.3242703 C124.362973,25.5314595 128.256486,29.1883784 134.293784,29.1883784 C137.82973,29.1883784 139.894865,28.1151892 141.524595,26.6841892 L138.465405,23.3849189 C137.631081,23.9811892 136.161081,24.7364595 134.214324,24.7364595 C131.790811,24.7364595 130.361351,23.7427297 129.844865,21.9937297 Z M129.765405,18.8931892 C130.202432,16.866 131.631892,15.9120811 133.738378,15.9120811 C135.843243,15.9120811 137.035135,17.0250811 137.272703,18.8931892 L129.765405,18.8931892 Z" id="Shape" fill="#FACC2B"></path>
          <path d="M12.4448919,5.99524054 C5.66632703,5.99524054 0.171030811,10.9249459 0.171030811,17.0061892 C0.171030811,19.2473514 0.919248649,21.3307297 2.20112432,23.0697568 C2.03273514,25.079027 1.54816216,27.9091622 0.171030811,29.2876216 C0.171030811,29.2876216 4.37897838,28.6966216 7.22951351,26.9742973 C8.81278378,27.6419189 10.5797838,28.0171622 12.4448919,28.0171622 C19.2235135,28.0171622 24.7187838,23.0874324 24.7187838,17.0061892 C24.7187838,10.9249459 19.2235135,5.99524054 12.4448919,5.99524054 Z" id="Path" fill="#FACC2B"></path>
          <path d="M12.4448919,5.99524054 C5.66632703,5.99524054 0.171030811,10.9249459 0.171030811,17.0061892 C0.171030811,19.2473514 0.919248649,21.3307297 2.20112432,23.0697568 C2.03273514,25.079027 1.54816216,27.9091622 0.171030811,29.2876216 C0.171030811,29.2876216 4.37897838,28.6966216 7.22951351,26.9742973 C8.81278378,27.6419189 10.5797838,28.0171622 12.4448919,28.0171622 C19.2235135,28.0171622 24.7187838,23.0874324 24.7187838,17.0061892 C24.7187838,10.9249459 19.2235135,5.99524054 12.4448919,5.99524054 Z" id="Path" fill="#4885ED"></path>
          <path d="M12.4421351,24.8694324 L12.7312703,24.8694324 L18.8872703,10.6898108 L16.0778919,10.6898108 L13.7228919,16.1052973 C13.1858108,17.3249189 12.6487297,19.2884595 12.6487297,19.2884595 C12.6487297,19.2884595 12.0908919,17.3041622 11.5538108,16.1052973 L9.13686486,10.6898108 L6.03832703,10.6898108 L12.4421351,24.8694324 Z" id="Path" fill="#FFFFFF"></path>
          <path d="M28.6454595,12.7881892 C28.6454595,6.70699459 23.1501892,1.77718703 16.3715676,1.77718703 C11.4767027,1.77718703 7.25202973,4.34843514 5.28135405,8.06723514 C7.29767838,6.76494324 9.7697027,5.99514324 12.4439189,5.99514324 C19.2225405,5.99514324 24.7178108,10.9248649 24.7178108,17.0061892 C24.7178108,19.3322432 23.9117027,21.4883514 22.5394054,23.2662162 C25.2882973,24.594973 28.6454595,25.0696216 28.6454595,25.0696216 C27.2682973,23.6915676 26.7837568,20.8614324 26.6153514,18.8517568 C27.8972432,17.1127297 28.6454595,15.0293514 28.6454595,12.7881892 Z" id="Path" fill="#FACC2B"></path>
        </g>
      </g>
    </g>
  </svg>
</a></span><span style="display: block;font-size: 10px !important; color: #333333; margin: 0px; text-align: center;flex: 1;padding: 0px;line-height: 1 !important;">Advertisement</span></div></div></div><div data-v-591f97f5="" class="level-item"><div data-v-591f97f5=""><div data-v-591f97f5="" class="has-text-centered">Thanks for using our</div><h1 data-v-591f97f5="" class="title has-text-centered is-marginless">Online Python 3 <!---->
            IDE</h1><div data-v-591f97f5="" class="has-text-centered margin-bottom-10px">to execute your program</div></div></div><div data-v-591f97f5="" id="vuukle-ad-6" class="level-item" style="min-width: 300px; min-height: 250px;"><div class="vuukle-ads" style="display: block;height: auto;margin: 0px auto;text-align: center;clear: both; width: 100%; max-width: 100%; overflow: hidden;"><div id="div-gpt-ad-1497448474263-6" data-google-query-id="CKuf0Ija-_gCFa6XlQIdYVYGSw"><div id="google_ads_iframe_/213794966,21668329608/vuukle-widget/jdoodle.com-6_0__container__" style="border: 0pt none; margin: auto; text-align: center; width: 300px; height: 250px;"><iframe frameborder="0" src="./minimax_files/container(1).html" id="google_ads_iframe_/213794966,21668329608/vuukle-widget/jdoodle.com-6_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" role="region" aria-label="Advertisement" tabindex="0" data-google-container-id="1" style="border: 0px; vertical-align: bottom; width: 300px !important; height: 250px !important;" data-load-complete="true"></iframe></div></div><div class="vuukle-ad-label" style="display: flex; justify-content: space-evenly; align-items: flex-end; flex-basis: 100%; margin: 0px auto; width: 300px; height: 11px; padding: 0px; line-height: 1.1 !important;"><span style="display: block;margin: 0px;line-height: 0 !important;padding: 0px;"><a aria-label="Vuukle" href="https://vuukle.com/" target="_blank" style="background-color: transparent; box-shadow: none;" rel="noopener nofollow">
  <svg width="11px" viewBox="0 0 30 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
      <g transform="translate(-150.000000, -31.000000)" fill-rule="nonzero">
        <g transform="translate(150.000000, 31.000000)">
          <path d="M41.8097027,29.0691892 L42.3657568,29.0691892 L54.204,1.80093081 L48.8013243,1.80093081 L44.2726216,12.2153514 C43.2397297,14.5605405 42.2069189,18.3368108 42.2069189,18.3368108 C42.2069189,18.3368108 41.1342973,14.5208108 40.1014865,12.2153514 L35.4535946,1.80093081 L29.4948649,1.80093081 L41.8097027,29.0691892 Z M59.7741892,29.1883784 C62.118,29.1883784 64.0645946,28.0754595 65.0974054,26.0481892 L64.9782162,28.8307297 L70.3412432,28.8307297 L70.3412432,11.8972703 L64.9782162,11.8972703 L64.9782162,20.9602703 C64.9782162,23.1067297 63.7864865,24.339 61.6413243,24.339 C59.7345405,24.339 58.8207568,23.226 58.8207568,21.318 L58.8207568,11.8972703 L53.4578919,11.8972703 L53.4578919,21.6757297 C53.4578919,26.4854595 56.0797297,29.1883784 59.7741892,29.1883784 Z M80.7617838,29.1883784 C83.1056757,29.1883784 85.0524324,28.0754595 86.0845946,26.0481892 L85.9662162,28.8307297 L91.3289189,28.8307297 L91.3289189,11.8972703 L85.9662162,11.8972703 L85.9662162,20.9602703 C85.9662162,23.1067297 84.7743243,24.339 82.6289189,24.339 C80.7218919,24.339 79.8081892,23.226 79.8081892,21.318 L79.8081892,11.8972703 L74.4458919,11.8972703 L74.4458919,21.6757297 C74.4458919,26.4854595 77.0671622,29.1883784 80.7617838,29.1883784 Z M100.915946,23.9414595 L102.345405,22.431 L106.556757,28.8307297 L112.793514,28.8307297 L106.158649,18.8138108 L112.157838,11.8972703 L106.198378,11.8972703 L100.637838,18.4162703 C100.796757,17.343 100.915946,16.0312703 100.915946,14.7592703 L100.915946,0.131416216 L95.5524324,0.131416216 L95.5524324,28.8307297 L100.915946,28.8307297 L100.915946,23.9414595 Z M115.301351,28.8307297 L120.624324,28.8307297 L120.624324,0.131416216 L115.301351,0.131416216 L115.301351,28.8307297 Z M129.844865,21.9937297 L142.675946,21.9937297 C143.073243,16.071 139.776486,11.5395405 133.697838,11.5395405 C128.454324,11.5395405 124.362973,15.1965405 124.362973,20.3242703 C124.362973,25.5314595 128.256486,29.1883784 134.293784,29.1883784 C137.82973,29.1883784 139.894865,28.1151892 141.524595,26.6841892 L138.465405,23.3849189 C137.631081,23.9811892 136.161081,24.7364595 134.214324,24.7364595 C131.790811,24.7364595 130.361351,23.7427297 129.844865,21.9937297 Z M129.765405,18.8931892 C130.202432,16.866 131.631892,15.9120811 133.738378,15.9120811 C135.843243,15.9120811 137.035135,17.0250811 137.272703,18.8931892 L129.765405,18.8931892 Z" id="Shape" fill="#FACC2B"></path>
          <path d="M12.4448919,5.99524054 C5.66632703,5.99524054 0.171030811,10.9249459 0.171030811,17.0061892 C0.171030811,19.2473514 0.919248649,21.3307297 2.20112432,23.0697568 C2.03273514,25.079027 1.54816216,27.9091622 0.171030811,29.2876216 C0.171030811,29.2876216 4.37897838,28.6966216 7.22951351,26.9742973 C8.81278378,27.6419189 10.5797838,28.0171622 12.4448919,28.0171622 C19.2235135,28.0171622 24.7187838,23.0874324 24.7187838,17.0061892 C24.7187838,10.9249459 19.2235135,5.99524054 12.4448919,5.99524054 Z" id="Path" fill="#FACC2B"></path>
          <path d="M12.4448919,5.99524054 C5.66632703,5.99524054 0.171030811,10.9249459 0.171030811,17.0061892 C0.171030811,19.2473514 0.919248649,21.3307297 2.20112432,23.0697568 C2.03273514,25.079027 1.54816216,27.9091622 0.171030811,29.2876216 C0.171030811,29.2876216 4.37897838,28.6966216 7.22951351,26.9742973 C8.81278378,27.6419189 10.5797838,28.0171622 12.4448919,28.0171622 C19.2235135,28.0171622 24.7187838,23.0874324 24.7187838,17.0061892 C24.7187838,10.9249459 19.2235135,5.99524054 12.4448919,5.99524054 Z" id="Path" fill="#4885ED"></path>
          <path d="M12.4421351,24.8694324 L12.7312703,24.8694324 L18.8872703,10.6898108 L16.0778919,10.6898108 L13.7228919,16.1052973 C13.1858108,17.3249189 12.6487297,19.2884595 12.6487297,19.2884595 C12.6487297,19.2884595 12.0908919,17.3041622 11.5538108,16.1052973 L9.13686486,10.6898108 L6.03832703,10.6898108 L12.4421351,24.8694324 Z" id="Path" fill="#FFFFFF"></path>
          <path d="M28.6454595,12.7881892 C28.6454595,6.70699459 23.1501892,1.77718703 16.3715676,1.77718703 C11.4767027,1.77718703 7.25202973,4.34843514 5.28135405,8.06723514 C7.29767838,6.76494324 9.7697027,5.99514324 12.4439189,5.99514324 C19.2225405,5.99514324 24.7178108,10.9248649 24.7178108,17.0061892 C24.7178108,19.3322432 23.9117027,21.4883514 22.5394054,23.2662162 C25.2882973,24.594973 28.6454595,25.0696216 28.6454595,25.0696216 C27.2682973,23.6915676 26.7837568,20.8614324 26.6153514,18.8517568 C27.8972432,17.1127297 28.6454595,15.0293514 28.6454595,12.7881892 Z" id="Path" fill="#FACC2B"></path>
        </g>
      </g>
    </g>
  </svg>
</a></span><span style="display: block;font-size: 10px !important; color: #333333; margin: 0px; text-align: center;flex: 1;padding: 0px;line-height: 1 !important;">Advertisement</span></div></div></div></div><div data-v-591f97f5="" class="columns is-mobile margin-top-10px"><div data-v-591f97f5="" class="column is-10-mobile is-offset-1-mobile is-8-tablet is-offset-2-tablet is-6-desktop is-offset-3-desktop has-text-centered comment-box has-text-weight-semibold"><div data-v-5cbc0b3b="" data-v-591f97f5="" class="margin-top-20px margin-bottom-10px has-text-centered"><div data-v-5cbc0b3b="" class="level has-text-centered"><div data-v-5cbc0b3b="" class="level-item store-img"><a data-v-5cbc0b3b="" href="https://play.google.com/store/apps/details?id=com.nutpan.jdoodle_app&amp;pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1" target="_blank"><img data-v-5cbc0b3b="" src="./minimax_files/google-play-badge.db9b21a1.png" alt="Get it on Google Play" class="google-store-img"></a></div><div data-v-5cbc0b3b="" class="level-item store-img"><a data-v-5cbc0b3b="" href="https://apps.apple.com/us/app/jdoodle/id1544598494" target="_blank"><img data-v-5cbc0b3b="" src="./minimax_files/Apple_Store_Badge.2928664f.svg" alt="Get it on Apple Store" class="apple-store-img"></a></div></div></div></div></div><div data-v-591f97f5="" class="columns"><div data-v-591f97f5="" class="column"><div data-v-72256225="" data-v-591f97f5="" class="know-box box has-text-centered comment-box has-text-weight-semibold"><div data-v-72256225="" class="has-text-centered is-underlined know-title">Know Your JDoodle</div><div data-v-72256225="" class="has-text-left"><ul data-v-72256225=""><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">JDoodle Supports 76+ Languages with Multiple Versions and 2 DBs. <a data-v-72256225="" class="is-link has-text-weight-bold"> Click here </a> to see all.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">Fullscreen - side-by-side code and output is available. click the "<svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="expand" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="svg-inline--fa fa-expand fa-w-14"><path data-v-72256225="" fill="currentColor" d="M0 180V56c0-13.3 10.7-24 24-24h124c6.6 0 12 5.4 12 12v40c0 6.6-5.4 12-12 12H64v84c0 6.6-5.4 12-12 12H12c-6.6 0-12-5.4-12-12zM288 44v40c0 6.6 5.4 12 12 12h84v84c0 6.6 5.4 12 12 12h40c6.6 0 12-5.4 12-12V56c0-13.3-10.7-24-24-24H300c-6.6 0-12 5.4-12 12zm148 276h-40c-6.6 0-12 5.4-12 12v84h-84c-6.6 0-12 5.4-12 12v40c0 6.6 5.4 12 12 12h124c13.3 0 24-10.7 24-24V332c0-6.6-5.4-12-12-12zM160 468v-40c0-6.6-5.4-12-12-12H64v-84c0-6.6-5.4-12-12-12H12c-6.6 0-12 5.4-12 12v124c0 13.3 10.7 24 24 24h124c6.6 0 12-5.4 12-12z" class=""></path></svg>" icon near execute button to switch.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">Dark Theme available. Click on "<svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="ellipsis-h" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="svg-inline--fa fa-ellipsis-h fa-w-16"><path data-v-72256225="" fill="currentColor" d="M328 256c0 39.8-32.2 72-72 72s-72-32.2-72-72 32.2-72 72-72 72 32.2 72 72zm104-72c-39.8 0-72 32.2-72 72s32.2 72 72 72 72-32.2 72-72-32.2-72-72-72zm-352 0c-39.8 0-72 32.2-72 72s32.2 72 72 72 72-32.2 72-72-32.2-72-72-72z" class=""></path></svg>" icon near execute button and select dark theme.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">You can embed code from JDoodle directly into your website/blog. <a data-v-72256225="" target="_blank" href="http://blog.nutpan.com/2016/07/run-programs-directly-from-your-blog-or.html" class="is-link has-text-weight-bold"> Click here </a> to know more.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">JDoodle offers an API service. You can execute programs just by calling our API.<a data-v-72256225="" target="_blank" href="https://www.jdoodle.com/compiler-api" class="is-link has-text-weight-bold"> Click here </a> to know more.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">If you like JDoodle, Please share us in Social Media.<a data-v-72256225="" target="_blank" class="is-link has-text-weight-bold"> Click here </a> to share.</span></li><li data-v-72256225=""><svg data-v-72256225="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-72256225="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-72256225="" class="li-points">Check our <a data-v-72256225="" target="_blank" href="https://docs.jdoodle.com/" class="is-link has-text-weight-bold"> Documentation Page </a> for more info.</span></li></ul><div data-v-72256225="" class="has-text-centered in-service">JDoodle is serving the programming community since 2013</div></div></div></div><div data-v-591f97f5="" class="column"><div data-v-92dc461c="" data-v-591f97f5="" class="know-box box has-text-centered comment-box has-text-weight-semibold"><div data-v-92dc461c="" class="has-text-centered is-underlined know-title">JDoodle For Your Organisation</div><div data-v-92dc461c="" class="has-text-left"><ul data-v-92dc461c=""><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Do you have any specific compiler requirements?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Do you want to integrate compilers with your website, webapp, mobile app, courses?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Do you need more than our <a data-v-92dc461c="" target="_blank" href="http://blog.nutpan.com/2016/07/run-programs-directly-from-your-blog-or.html" class="is-link has-text-weight-bold"> Embed </a> and <a data-v-92dc461c="" target="_blank" href="https://www.jdoodle.com/compiler-api" class="is-link has-text-weight-bold"> API </a> features?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Looking for Multiple Files, Connecting to DB, Debugging, etc.?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Are you building any innovative solution for your students or recruitment?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Want to run JDoodle in-house?</span></li><li data-v-92dc461c=""><svg data-v-92dc461c="" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="dot-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="has-text-grey-dark svg-inline--fa fa-dot-circle fa-w-16"><path data-v-92dc461c="" fill="currentColor" d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm80 248c0 44.112-35.888 80-80 80s-80-35.888-80-80 35.888-80 80-80 80 35.888 80 80z" class=""></path></svg><span data-v-92dc461c="" class="li-points">Custom Domain, White labelled pages for your institute?</span></li></ul></div><div data-v-92dc461c="" class="has-text-centered in-service">Contact us - We are happy to help!</div></div></div></div><div data-v-d20fc626="" data-v-591f97f5="" class="is-hidden-print"><div data-v-d20fc626="" class="has-text-centered comment-box-title has-text-weight-semibold">Your valuable input will help us improve this site <br data-v-d20fc626=""> please give your comments. Thanks.</div><div data-v-d20fc626="" class="container"><div data-v-d20fc626="" class="columns is-mobile"><div data-v-d20fc626="" class="column is-10-mobile is-offset-1-mobile is-8-tablet is-offset-2-tablet is-6-desktop is-offset-3-desktop box has-text-centered comment-box has-text-weight-semibold"><div data-v-d20fc626="" class="other-languages"><a data-v-d20fc626="" class="is-link has-text-weight-bold">
            Click here
          </a>
          to see the languages currently supported.
        </div><div data-v-d20fc626="" class="what-next">Which language would you like to see next in JDoodle?</div><div data-v-d20fc626=""><div data-v-d20fc626="" class="columns"><div data-v-d20fc626="" class="column"><div data-v-d20fc626="" class="field has-addons"><div data-v-d20fc626="" class="control is-expanded"><input data-v-d20fc626="" data-vv-as="Language" name="language" type="text" maxlength="50" placeholder="New Language" class="input input" aria-required="true" aria-invalid="false"></div><div data-v-d20fc626="" class="control"><button data-v-d20fc626="" class="button has-text-weight-bold">
                    Add This
                  </button></div></div><div data-v-d20fc626=""><span data-v-d20fc626="" class="help is-danger" style="display: none;"></span></div></div></div><div data-v-d20fc626="" class="what-next what-next-thanks" style="display: none;">
            Thanks for your Input!
          </div><div data-v-d20fc626="" class="what-next what-next-thanks" style="display: none;">
             is already available at <a data-v-d20fc626="" href="https://www.jdoodle.com/python3-programming-online/"></a></div></div><div data-v-d20fc626="" class="what-next">Comments/Suggestions/Inputs...</div><div data-v-d20fc626="" class="columns"><div data-v-d20fc626="" class="column"><textarea data-v-d20fc626="" data-vv-as="Comment" name="comment" rows="6" class="textarea input" aria-required="true" aria-invalid="false"></textarea><span data-v-d20fc626="" class="help is-danger" style="display: none;"></span><div data-v-d20fc626="" class="is-size-7 note">For direct response, please include your email id in the comment <br data-v-d20fc626=""> or email to
              <a data-v-d20fc626="" href="mailto:hello@jdoodle.com">hello@jdoodle.com</a></div><button data-v-d20fc626="" type="button" class="button has-text-weight-bold">Post Comment
            </button></div></div><div data-v-d20fc626="" class="what-next what-next-thanks has-text-centered" style="display: none;">
          Thanks for your Input!
        </div></div></div></div></div></div></div><!----><footer data-v-c6b17094="" class="footer has-text-weight-semibold is-hidden-print" isdark="python3"><div data-v-c6b17094="" class="contact-us">contact us at <a data-v-c6b17094="" href="mailto:hello@jdoodle.com" id="contact-us">hello@jdoodle.com</a></div><div data-v-c6b17094="" class="copyright">© 2013-2022 Nutpan pty Ltd. All Rights Reserved.</div><div data-v-c6b17094="" class="twitterfollow"><a data-v-c6b17094="" href="https://twitter.com/thenutpan" rel="nofollow" data-show-count="false" data-show-screen-name="false" class="twitter-follow-button">Follow @thenutpan</a></div><div data-v-c6b17094=""><span data-v-c6b17094="" class="text-info">JDoodle uses cookies</span>. Please read full <a data-v-c6b17094="" href="https://www.jdoodle.com/terms">Terms of Use</a> before using this service.</div></footer></div><script>window.TogetherJSConfig_hubBase = 'https://tjhub.jdoodle.com/'
      window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
      ga('create', 'UA-42395517-1', 'auto');
      window.TogetherJSConfig_hubBase = 'https://tjhub.jdoodle.com/'</script><script async="" src="./minimax_files/analytics.js.download"></script><script async="" src="./minimax_files/togetherjs-min.js.download"></script><script async="" src="./minimax_files/api.js.download"></script><script src="./minimax_files/chunk-vendors.efd56467.js.download"></script><script src="./minimax_files/app.87c94515.js.download"></script><div id="1afb08486ae342638ec7de970117e35d"></div><script type="text/javascript" async="" src="./minimax_files/ace.min.js.download"></script><script type="text/javascript" async="" src="./minimax_files/platform.js.download"></script><script type="text/javascript" async="" src="./minimax_files/ext-language_tools.js.download"></script><script type="text/javascript" async="" src="./minimax_files/ext-static_highlight.js.download"></script><iframe src="./minimax_files/container(2).html" style="visibility: hidden; display: none;"></iframe><iframe style="display: none;" src="./minimax_files/saved_resource(1).html"></iframe><iframe src="javascript:false" style="width: 1px; height: 1px; border: 0px; margin: 0px;" src="./minimax_files/saved_resource(2).html"></iframe><div style="visibility: hidden; position: absolute; width: 100%; top: -10000px; left: 0px; right: 0px; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.5;"></div><div style="margin: 0px auto; top: 0px; left: 0px; right: 0px; position: absolute; border: 1px solid rgb(204, 204, 204); z-index: 2000000000; background-color: rgb(255, 255, 255); overflow: hidden;"><iframe title="o desafio reCAPTCHA expira em dois minutos" src="./minimax_files/bframe.html" name="c-iwnbz6rwtfmt" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox" style="width: 100%; height: 100%;"></iframe></div></div><iframe src="./minimax_files/aframe.html" width="0" height="0" style="display: none;"></iframe><div><iframe src="./minimax_files/pd.html" width="0" height="0" style="display:none;"></iframe></div></body></html>