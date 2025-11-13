{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  languages.python.enable = true;
  languages.python.uv.enable = true;
}
