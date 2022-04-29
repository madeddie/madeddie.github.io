function FindProxyForURL (url, host) {
  if (isPlainHostName(host))
    return 'DIRECT';
  else
    return 'PROXY 198.18.7.3:8888';
}
