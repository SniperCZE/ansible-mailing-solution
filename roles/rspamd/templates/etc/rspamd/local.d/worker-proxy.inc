bind_socket = "{{rspamd_server_hostname}}:11332";
milter = yes;
timeout = 120s;
upstream "local" {
  default = yes;
  self_scan = yes;
}
